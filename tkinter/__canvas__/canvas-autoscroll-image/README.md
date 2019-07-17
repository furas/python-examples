Image is moving up and down.

This example use 

 - module PIL/pillow to load jpg/png instead of gif
 - `after(time_in_millisecond, function_name)` to repeat function which moves image
 - `img_id` to use only one image (instead of creating many images with `create_image`)
 - `canvas.move(ID, offset_x, offset_y)` to move image (or other object) 
 - `canvas.coords(ID)` to get current positon of image (or other object)
 - `canvas.pack(fill='both', expand=True)` to use full window. Canvas will use full window even when you resize window.

You can use also `canvas.coords(ID, x+offset_x, y+offset_y)` instead of `canvas.move(ID, offset_x, offset_y)` to set new position.

