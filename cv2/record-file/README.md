Recording camera stream in file(s)

- display menu
- check keys (R - record, S - stop, Q - quit, ESC - quit)   
- record in (many) file(s) (10MB in every file)
- (optional) display in two windows - with and without menu (one hidden behind another)

---

To save in file you have to set correct `width`, `height` in `cv2.VideoWriter`.

If input stream is `1024x768` then it can't be saved as `640x480` without manual resizing frame.

