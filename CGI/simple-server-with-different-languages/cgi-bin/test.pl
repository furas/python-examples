#!/usr/bin/env perl
print "Content-Type: text/html; charset=utf-8\n";
print "\n";

# "Content-Type" has to be in first line - without even empty lines 
# after headers have to be empty line

$result = 1 + 2;

print  <<ENDHTML
<!DOCTYPE html>

<html>

<head>
    <meta charset="utf-8"/>
    <title>Perl</title>
    <style>
        body {background-color:#ddd; text-align: center}
    </style>     
</head>

<body>

    <h1>PERL</h1>

    <h2>1 + 2 = $result</h2>
    
    <a href="/images/transparent.png"><img src="/images/transparent.png"><br/>/images/transparent.png</a><br/>
    <br/>
    
    <a href="/cgi-bin/image.png"><img src="/cgi-bin/image.png"><br/>/cgi-bin/image.png</a><br/>
    (python script with extension .png)<br/>
       
</body>

</html>
ENDHTML
