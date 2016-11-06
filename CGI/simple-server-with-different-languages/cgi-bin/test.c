#include <stdio.h>

int main()
{
    int result;

    printf("Content-Type: text/html; charset=utf-8\n");
    printf("\n");

    /* "Content-Type" has to be in first line - without even empty lines */
    /* after headers have to be empty line */

    result = 1 + 2;

    printf("<!DOCTYPE html>\n\
\n\
<html>\n\
\n\
<head>\n\
    <meta charset=\"utf-8\"/>\n\
    <title>C</title>\n\
    <style>\n\
        body {background-color:#ddd; text-align: center}\n\
    </style>\n\
</head>\n\
\n\
<body>\n\
\n\
    <h1>C</h1>\n\
\n\
    <h2>1 + 2 = %i</h2>\n\
\n\
    <a href=\"/images/transparent.png\"><img src=\"/images/transparent.png\"><br/>/images/transparent.png</a><br/>\n\
    <br/>\n\
\n\
    <a href=\"/cgi-bin/image.png\"><img src=\"/cgi-bin/image.png\"><br/>/cgi-bin/image.png</a><br/>\n\
    (python script with extension .png)<br/>\n\
\n\
</body>\n\
\n\
</html>", result);

    return 0;
}

/* it needs ' \" ' */
