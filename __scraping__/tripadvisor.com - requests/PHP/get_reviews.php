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

//---------------------------------------------------------------------
// Get HTML page from server and convert to DOMXpath 
// to search in HTML using XPath
//---------------------------------------------------------------------

function get_soup($url) {
    echo '[get_soup] url: ', $url, "\n";

    // for test - to see what you get from server
    // $html = file_get_contents($url);
    // echo $html
    
    // read HTML directly from server and convert to DOMDocument
    $doc = new DOMDocument();
    $doc->loadHTMLFile($url, LIBXML_NOERROR);

    // search in HTML using XPath
    $xpath = new DOMXPath($doc);
    
    return $xpath;
}

//---------------------------------------------------------------------
// get number of reviews and start parsing every subpage with reviews
//---------------------------------------------------------------------

function parse($url, $xpath){
    echo '[parse] url: ', $url, "\n";
    
    // get number of reviews in all languages
    $num_reviews = $xpath->query('//span[@class="reviews_header_count"]/text()')[0]->nodeValue; // get text
    $num_reviews = substr($num_reviews, 1, -1); // remove `( )`
    $num_reviews = str_replace(',', '', $num_reviews); // remove `,`
    $num_reviews = (int)$num_reviews; // convert text into integer
    echo '[parse] num_reviews ALL: ', $num_reviews, "\n";
    
    // get number of reviews in English
    $num_reviews = $xpath->query('//div[@data-value="en"]//span/text()')[0]->nodeValue; // get text
    $num_reviews = substr($num_reviews, 1, -1); // remove `( )`
    $num_reviews = str_replace(',', '', $num_reviews); // remove `,`
    $num_reviews = (int)$num_reviews; // convert text into integer
    echo '[parse] num_reviews ENGLISH: ', $num_reviews, "\n";
    
    // create template url for subpages with reviews
    // ie. https://www.tripadvisor.com/Hotel_Review-g562819-d289642-or{}.html
    $url_template = str_replace('.html', '-or{}.html', $url);
    echo '[parse] url_template:', $url_template;
    
    // create subpages urls and parse reviewes.
    // every subpage has 5 reviews and it has url with -or0.html -or5.html -or10.html -or15.html etc.
    for($offset = 0 ; $offset < $num_reviews ; $offset += 5) {
        $subpage_url = str_replace('{}', $offset, $url_template);
        
        echo '[parse] subpage_url: ', $subpage_url;
        
        parse_reviews($subpage_url, get_soup($subpage_url));
        
        //~ return; // for test only - to stop after first page    
    }
}

//---------------------------------------------------------------------
// find all reviews on subpage
//---------------------------------------------------------------------

function parse_reviews($url, $xpath) {
    echo '[parse_reviews] url: ', $url, "\n";
    
    // find hotel name
    $hotel_name = $xpath->query('//h1[@id="HEADING"]/text()')[0]->nodeValue;
    
    // find all reviews on page 
    foreach($xpath->query('//div[@class="review-container"]') as $review) {
        
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
        
        // append to CSV file 
        global $csv_file; 
        fputcsv($csv_file, $item);
        
        // display on screen 
        echo "\n", '--- review ---', "\n\n";
        
        foreach($item as $key => $val) {
            echo $key, ': ', $val, "\n";
        }
        
        //~ return; // for test only - to stop after first review
    }
    
    echo "\n"; # empty line after last review
}

//---------------------------------------------------------------------
// START 
//---------------------------------------------------------------------

// some URLs for testing
$start_urls = [
    'https://www.tripadvisor.com/Hotel_Review-g562819-d289642-Reviews-Hotel_Caserio-Playa_del_Ingles_Maspalomas_Gran_Canaria_Canary_Islands.html',
    'https://www.tripadvisor.com/Hotel_Review-g60795-d102542-Reviews-Courtyard_Philadelphia_Airport-Philadelphia_Pennsylvania.html',
    //'https://www.tripadvisor.com/Hotel_Review-g60795-d122332-Reviews-The_Ritz_Carlton_Philadelphia-Philadelphia_Pennsylvania.html',
];

// create empty CSV file
$csv_file = fopen('results.csv', 'w');

// write headers
fputcsv($csv_file, ['hotel name', 'review title', 'review body', 'review date', 'contributions', 'helpful vote', 'user name' , 'user location', 'rating']);

// run code for every URL from list
foreach($start_urls as $url) {
    parse($url, get_soup($url));
}

// close CSV file
fclose($csv_file);

?>
