<?php

//---------------------------------------------------------------------
// PHP manual
//---------------------------------------------------------------------
// http://php.net/manual/en/book.dom.php
// http://php.net/manual/en/class.domdocument.php
// http://php.net/manual/en/class.domtext.php
// http://php.net/manual/en/class.domxpath.php
// http://php.net/manual/en/domxpath.query.php
// http://php.net/manual/en/function.fputcsv.php
//---------------------------------------------------------------------

// https://stackoverflow.com/questions/3431160/php-send-cookie-with-file-get-contents

// https://stackoverflow.com/questions/4690417/php-how-to-perform-an-http-request-passing-cookies-and-save-result-to-a-string?lq=1
// https://stackoverflow.com/questions/2138527/php-curl-http-post-sample-code
// http://php.net/manual/en/curl.examples-basic.php

class Request {

    $cookies = []
    $headers = []
    
    function get($url, $params)
        $ch = curl_init();
        curl_setopt($ch, CURLOPT_URL, $url);
        curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);

        curl_setopt($ch, CURLOPT_COOKIEJAR, '/tmp/cookies.txt');
        curl_setopt($ch, CURLOPT_COOKIEFILE, '/tmp/cookies.txt');

        $output = curl_exec($ch);
        $info = curl_getinfo($ch);
        curl_close($ch);
    }

    function get($url, $params)
        $ch = curl_init();
        curl_setopt($ch, CURLOPT_URL, $url);
        curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);

        curl_setopt($ch, CURLOPT_COOKIEJAR, '/tmp/cookies.txt');
        curl_setopt($ch, CURLOPT_COOKIEFILE, '/tmp/cookies.txt');

        $output = curl_exec($ch);
        $info = curl_getinfo($ch);
        curl_close($ch);
    }

}

//---------------------------------------------------------------------
// Get HTML page from server using GET request
// and convert to DOMXPath to search in HTML using XPath
//---------------------------------------------------------------------

function get_soup($url) {
    echo '[get_soup] url: ', $url, "\n";

    // for test - to see what you get from server
    // $html = file_get_contents($url);
    // echo $html
    // $doc = new DOMDocument();
    // $doc->loadHTML($html, LIBXML_NOERROR);
    
    // read HTML directly from server and convert to DOMDocument
    $doc = new DOMDocument();
    $doc->loadHTMLFile($url, LIBXML_NOERROR);

    // search in HTML using XPath
    $xpath = new DOMXPath($doc);
    
    return $xpath;
}

//---------------------------------------------------------------------
// Get HTML page from server using POST request
// and convert to DOMXPath to search in HTML using XPath
//---------------------------------------------------------------------

function post_soup($url, $params) {
    echo '[psot_soup] url: ', $url, "\n";

    $postdata = http_build_query($params);

    $opts = array('http' =>
        array(
            'method'  => 'POST',
            'header'  => 'Content-type: application/x-www-form-urlencoded',
            'content' => $postdata
        )
    );

    $context  = stream_context_create($opts);

    $html = file_get_contents($url, false, $context);
    
    // read HTML directly from server and convert to DOMDocument
    $doc = new DOMDocument();
    $doc->loadHTML($html, LIBXML_NOERROR);

    // search in HTML using XPath
    $xpath = new DOMXPath($doc);
    
    return $xpath;
}

//---------------------------------------------------------------------

function scrape($url, $lang='ALL') {

    //~ # create session to keep all cookies (etc.) between requests
    //~ $session = requests.Session();

    //~ $session.headers.update({
        //~ # some portals send correct HTML only if you have correct header 'user-agent'
        //~ 'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:57.0) Gecko/20100101 Firefox/57.0',
    //~ });

    //~ # add '?filterLang=ALL' to url to get all reviews (not only English)
    //~ # add '?filterLang=es'  to url to get Spanish reviews
    //~ # add '?filterLang=pl'  to url to get Polish reviews
    //~ # etc.
    //~ # ie. https://www.tripadvisor.com/Hotel_Review-g562819-d289642-Reviews-Hotel_Caserio-Playa_del_Ingles_Maspalomas_Gran_Canaria_Canary_Islands.html?filterLang=ALL'
    //~ # for test - check language in cookies

    $items = parse($url . '?filterLang=' . $lang);

    return $items;
}

//---------------------------------------------------------------------
// get number of reviews and start parsing every subpage with reviews
//---------------------------------------------------------------------

function parse($url){
    
    echo '[parse] url: ', $url, "\n";
    
    $xpath = get_soup($url);
    
    // get number of reviews in all languages
    $num_reviews = $xpath->query('//span[@class="reviews_header_count"]/text()')[0]->nodeValue; // get text
    $num_reviews = substr($num_reviews, 1, -1); // remove `( )`
    $num_reviews = str_replace(',', '', $num_reviews); // remove `,`
    $num_reviews = (int)$num_reviews; // convert text into integer
    echo '[parse] num_reviews ALL: ', $num_reviews, "\n";
    
    // get number of reviews in English
    //~ $num_reviews = $xpath->query('//div[@data-value="en"]//span/text()')[0]->nodeValue; // get text
    //~ $num_reviews = substr($num_reviews, 1, -1); // remove `( )`
    //~ $num_reviews = str_replace(',', '', $num_reviews); // remove `,`
    //~ $num_reviews = (int)$num_reviews; // convert text into integer
    //~ echo '[parse] num_reviews ENGLISH: ', $num_reviews, "\n";
    
    // create template url for subpages with reviews
    // ie. https://www.tripadvisor.com/Hotel_Review-g562819-d289642-or{}.html
    $url_template = str_replace('.html', '-or{}.html', $url);
    echo '[parse] url_template:', $url_template;
    
    // create subpages urls and parse reviewes.
    // every subpage has 5 reviews and it has url with -or0.html -or5.html -or10.html -or15.html etc.
    
    $items = [];
    
    $offset = 0;
    
    while(True) {
        $subpage_url = str_replace('{}', $offset, $url_template);
        
        $subpage_items = parse_reviews($subpage_url);
        
        if($subpage_items->length == 0) break;
        
        $items += $subpage_items;
        
        $offset += 5;

        //~ return $items; // for test only - to stop after first page    
    }  
    
    return $items;
}
#----------------------------------------------------------------------

function get_reviews_ids($xpath) {

    $reviews_ids = [];

    $items = $xpath->query('//div[@data-reviewid]');
    
    foreach($items as $x) {
        $id = $x->getAttribute('data-reviewid');
        if(in_array($id, $reviews_ids)) {
            $reviews_ids.push($id);
        }
    }
    
    echo '[get_reviews_ids] data-reviewid: ', var_dump($reviews_ids);
    
    return $reviews_ids;
}

#----------------------------------------------------------------------

function get_more($reviews_ids) {

    $url = 'https://www.tripadvisor.com/OverlayWidgetAjax?Mode=EXPANDED_HOTEL_REVIEWS_RESP&metaReferer=Hotel_Review';

    $reviews = implode(',', $reviews_ids);
    
    $payload = [
        'reviews' => $reviews, # ie. "577882734,577547902,577300887",
        #'contextChoice' => 'DETAIL_HR', # ???
        'widgetChoice' => 'EXPANDED_HOTEL_REVIEW_HSX', # ???
        'haveJses' => 'earlyRequireDefine,amdearly,global_error,long_lived_global,apg-Hotel_Review,apg-Hotel_Review-in,bootstrap,desktop-rooms-guests-dust-en_US,responsive-calendar-templates-dust-en_US,taevents',
        'haveCsses' => 'apg-Hotel_Review-in',
        'Action' => 'install',
    ];

    $xpath = post_soup($url, $payload);

    return $xpath;
}

//---------------------------------------------------------------------
// find all reviews on subpage
//---------------------------------------------------------------------

function parse_reviews($url) {
    echo '[parse_reviews] url: ', $url, "\n";
    
    $xpath = get_soup($url);
    
    // find hotel name
    $hotel_name = $xpath->query('//h1[@id="HEADING"]/text()')[0]->nodeValue;
    
    $reviews_ids = get_reviews_ids($xpath);
    $xpath = get_more($reviews_ids);

    $items = [];
    
    // find all reviews on page 
    //foreach($xpath->query('//div[@class="review-container"]') as $review) { # reviews on normal page
    foreach($xpath->query('//div[@class="reviewSelector"]') as $review) { # reviews on normal page
        
        // it has to check if `badgets` (contributions/helpful_vote) exist on page 
        $badgets = $xpath->query('.//span[@class="badgetext"]', $review);
        
        if($badgets->length > 1) {
            $contributions = $xpath->query('.//text()', $badgets[0])[0]->nodeValue;
            $helpful_vote  = $xpath->query('.//text()', $badgets[1])[0]->nodeValue;
        } elseif($badgets->length > 0) {
            $contributions = $xpath->query('.//text()', $badgets[0])[0]->nodeValue;
            $helpful_vote  = 0;
        } else {
            $contributions = 0;
            $helpful_vote  = 0;         
        };
        
        // it has to check if `user_loc` exists on page
        $user_loc = $xpath->query('.//div[@class="userLoc"]/strong/text()', $review);
        
        if($user_loc->length > 0) {
            $user_loc = $user_loc[0]->nodeValue;
        } else {
            $user_loc = '';
        }
        
        // it has to find value in class name (ie. "bubble_40" => "40", "bubble_50" => "50")
        $bubble_rating = $xpath->query('.//span[contains(@class, "ui_bubble_rating")]', $review)[0]->getAttribute('class');
        $bubble_rating = end(explode('_', $bubble_rating));
        
        $item = [
            'hotel_name'    => $hotel_name,
            
            'review_title'  => $xpath->query('.//span[@class="noQuotes"]/text()', $review)[0]->nodeValue,
            'review_body'   => $xpath->query('.//p[@class="partial_entry"]/text()', $review)[0]->nodeValue,
            'review_date'   => $xpath->query('.//span[@class="ratingDate"]', $review)[0]->getAttribute('title'),
            
            'contributions' => $contributions, 
            'helpful_vote'  => $helpful_vote,
            
            'user_name'     => $xpath->query('.//div[@class="info_text"]/div/text()', $review)[0]->nodeValue,
            'user_loc'      => $user_loc,
            
            'bubble_rating' => $bubble_rating,
        ];
        
        $items.push($item);
        
        // display on screen 
        echo "\n", '--- review ---', "\n\n";
        
        foreach($item as $key => $val) {
            echo $key, ': ', $val, "\n";
        }
        
        //~ return; // for test only - to stop after first review
    }
    
    echo "\n"; # empty line after last review
    
    return $items;
}

#----------------------------------------------------------------------

function write_in_csv($items, $filename='results.csv',
                  $headers=['hotel name', 'review title', 'review body',
                           'review date', 'contributions', 'helpful vote',
                           'user name' , 'user location', 'rating'],
                  $mode='w') {

    // create empty CSV file
    $csv_file = fopen($filename, $mode);

    // write headers
    if($mode == 'w') { # don't write headers if you append to existing file
        fputcsv($csv_file, $headers);
    }

    // close CSV file
    fclose($csv_file);
}

//---------------------------------------------------------------------

function main() {

    # some URLs for testing
    $start_urls = [
        'https://www.tripadvisor.com/Hotel_Review-g294229-d481832-Reviews-Pullman_Jakarta_Indonesia-Jakarta_Java.html',
        #'https://www.tripadvisor.com/Hotel_Review-g562819-d289642-Reviews-Hotel_Caserio-Playa_del_Ingles_Maspalomas_Gran_Canaria_Canary_Islands.html',
        #'https://www.tripadvisor.com/Hotel_Review-g60795-d102542-Reviews-Courtyard_Philadelphia_Airport-Philadelphia_Pennsylvania.html',
        #'https://www.tripadvisor.com/Hotel_Review-g60795-d122332-Reviews-The_Ritz_Carlton_Philadelphia-Philadelphia_Pennsylvania.html',
    ];

    $lang = 'in'; // indonesian

    foreach($start_urls as $url) {

        $part = explode('Reviews-', substr($url, 0, -5));
        $part = end($part);
        $filename = $part . '__' . $lang;
        echo 'filename: ', $filename, "\n";

        $items = scrape($url, $lang);

        if($items->length == 0) {
            echo 'No reviews', "\n";
        } else {
            write_in_csv($items, $filename . '.csv', $mode='w');
        }
    }
}

function get_reviews() {
    
    $url = 'https://www.tripadvisor.com/Hotel_Review-g294229-d481832-Reviews-Pullman_Jakarta_Indonesia-Jakarta_Java.html';
    $lang = 'in'; // indonesian
    
    $items = scrape($url, $lang);
    
    foreach($items as $item) {
        echo $item['review body'], "\n";
    }
}

//---------------------------------------------------------------------
// START 
//---------------------------------------------------------------------

//main();

// or

get_reviews();

?>
