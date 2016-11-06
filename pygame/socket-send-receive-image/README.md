Server use loop to send image with current time. First it sends 4 bytes with image size and later it send image.

Client use loop to receive image with current time (and display it). First it receive 4 bytes wiht image size and later it uses this information to receive image in chunks.


