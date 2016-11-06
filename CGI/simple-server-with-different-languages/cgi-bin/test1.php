#!/usr/bin/env php
<?php
echo "Content-Type: text/html; charset=utf-8\n";
echo "\n";

$result = 1 + 2; 

?>
<!DOCTYPE html>

<html>

<head>
    <meta charset="utf-8"/>
    <title>PHP</title>
    <style>
        body {background-color:#ddd; text-align: center}
    </style>    
</head>

<body>
    
    <h1>PHP 1</h1>

    <h2>1 + 2 = <?php echo $result; ?></h2>
    
    <a href="/images/transparent.png"><img src="/images/transparent.png"><br/>/images/transparent.png</a><br/>
    <br/>
    
    <a href="/cgi-bin/image.png"><img src="/cgi-bin/image.png"><br/>/cgi-bin/image.png</a><br/>
    (python script with extension .png)<br/>

</body>

</html>
