This code use cv2 to get stream and PyGame to display it.

One version blits directly on `screen` so window must have the same size as stream.

Other version blits on `Surface` and later blit `Surface` on `screen` so window may have different size.
