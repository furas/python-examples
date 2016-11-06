#!/usr/bin/env php
Content-Type: text/html; charset=utf-8

<!-- "Content-Type" has to be in first line - without even empty lines -->
<!-- after headers have to be empty line -->

<?php $result = 1 + 2; ?>

<!DOCTYPE html>

<html>

<head>
    <meta charset="utf-8"/>
    <title>PHP 2</title>
    <style>
        body {background-color:#ddd; text-align: center}
    </style>      
</head>

<body>
    
    <h1>PHP 2</h1>

    <h2>1 + 2 = <?php echo $result; ?></h2>
    
    <a href="/images/transparent.png"><img src="/images/transparent.png"><br/>/images/transparent.png</a><br/>
    <br/>
    
    <a href="/cgi-bin/image.png"><img src="/cgi-bin/image.png"><br/>/cgi-bin/image.png</a><br/>
    (python script with extension .png)<br/>
    
</body>

</html>

<!-- This is HTML commend, not PHP comment -->
<?php // This is PHP commend, not HTML comment ?>

