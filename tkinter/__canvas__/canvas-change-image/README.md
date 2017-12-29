
Add `image` to `canvas`:

    self.object_id = self.canvas.create_image(0, 0, image=...)

Change image:

    self.canvas.itemconfig(self.object_id, image=...)

Result:
 
![#1](animation/out.gif?raw=true)   
