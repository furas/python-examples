Server uses loop to send image with current time.  
In every loop first it sends 4 bytes with image's size and later it sends image.

Client uses loop to receive image with current time (and display it).  
In every loop first it receives 4 bytes with image's size and later it uses this information 
to receive image in chunks.


