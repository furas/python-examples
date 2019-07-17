This example shows how to convert `numpy array` to `PIL.Image` 
and then use it with `io.BytesIO` to create file `PNG` in memory.

And then it uses `send_file()` to send this `PNG` to client.

It also shows how to get image and put on `canvas`, and convert to `ImageData`

![#1](images/image.png?raw=true)

More about Canvas: [Pixel manipulation with canvas](https://developer.mozilla.org/en-US/docs/Web/API/Canvas_API/Tutorial/Pixel_manipulation_with_canvas)
