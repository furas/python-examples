Date: 2018.05.07
Portal: [http://www.tripadvisor.com](www.tripadvisor.com)

# tripadvisor.com - using `PHP`

I rewrote Python example in PHP.

It uses only standard functions and classes.

- file_get_contents()
- DOMDocument
- DOMXPath
- DOMText
- fileputcsv()

It saves in CSV file 

- hotel name
- review title
- review body
- review date
- number of contributions
- number of helpful vote
- user name (reviewer)
- user location (reviewer)
- (bubble) rating

---

PHP Manual:
- [Document Object Model](http://php.net/manual/en/book.dom.php)
- [DOMDocument class](http://php.net/manual/en/class.domdocument.php)
- [DOMText class](http://php.net/manual/en/class.domtext.php)
- [DOMXPath class](http://php.net/manual/en/class.domxpath.php)
- [DOMXPath::query](http://php.net/manual/en/domxpath.query.php)
- [fputcsv](http://php.net/manual/en/function.fputcsv.php)
- [file_get_contents](http://php.net/manual/en/function.file-get-contents.php)
