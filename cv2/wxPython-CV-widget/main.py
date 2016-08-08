import wx
import cv2

#---------------------------------------------------------------------- 
# Panel to display image from camera
#---------------------------------------------------------------------- 

class WebcamPanel(wx.Window): # wx.Panel, wx.Control
    
    def __init__(self, parent, camera, fps=10, flip=False):
        wx.Window.__init__(self, parent)

        # remember arguments
        self.camera = camera
        self.fps = fps
        self.flip = flip

        # get frame size
        ret_value, frame = self.camera.read()
        height, width = frame.shape[:2]

        # resize panel with camera image
        self.SetSize( (width, height) )
        #self.SetMinSize( (width, height) )
        
        # resize main window
        #self.GetParent().GetParent().SetSize( (width, height+37) ) # wymaga poprawki aby nie trzeba bylo dawac +37
        #self.GetGrandParent().SetSize( (width, height+25) )
        #self.GetTopLevelParent().SetSize( (width, height+25) ) # wrong parent
        
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        
        if self.flip:
            frame = cv2.flip(frame, 1)

        # create bitmap with frame
        self.bmp = wx.BitmapFromBuffer(width, height, frame)

        # timer to refresh frames
        self.timer = wx.Timer(self)
        self.timer.Start(1000./fps)

        # add functions to events 
        self.Bind(wx.EVT_PAINT, self.OnPaint)   # run when it is needed
        self.Bind(wx.EVT_TIMER, self.NextFrame) # run by timer


    def OnPaint(self, event):
        dc = wx.BufferedPaintDC(self)
        dc.DrawBitmap(self.bmp, 0, 0)

        
    def NextFrame(self, event):
        ret_value, frame = self.camera.read()
        if ret_value:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            if self.flip:
                frame = cv2.flip(frame, 1)
            self.bmp.CopyFromBuffer(frame)
            self.Refresh()

#----------------------------------------------------------------------
# Main Window
#---------------------------------------------------------------------- 
    
class MainWindow(wx.Frame):

    def __init__(self, camera, fps=10):
        wx.Frame.__init__(self, None)

        self.panel = wx.Panel(self, -1)

        # add sizer 
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.panel.SetSizer(self.sizer)
        
        # add button
        self.button = wx.Button(self.panel, label="CAPTURE")
        self.button.Bind(wx.EVT_BUTTON, self.OnButton)
        self.sizer.Add(self.button, 0, wx.EXPAND)

        # add panel with webcam image
        self.webcampanel = WebcamPanel(self.panel, camera)
        self.sizer.Add(self.webcampanel, 1, wx.EXPAND)

        #self.sizer.Layout()
        #self.webcampanel.Layout()
        #self.Fit()
        self.Show()
        
    def OnButton(self, event):
        print("TODO: save image in file")

        
#----------------------------------------------------------------------

camera = cv2.VideoCapture(0)

app = wx.App()
MainWindow(camera)
app.MainLoop()
