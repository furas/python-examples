import wx

class Example(wx.Frame):
    
    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)
        self.InitUI()

    def InitUI(self):
            
        img_color = wx.Image('Obrazy/furas.png')
        img_grey = img_color.ConvertToGreyscale(0.3, 0.3, 0.3)
        
        self.hbox = wx.BoxSizer(wx.HORIZONTAL)
        
        self.panel = wx.Panel(self)
        self.panel.SetSizer(self.hbox)

        self.bitmap_color = wx.Bitmap(img_color)
        self.bitmap_grey = wx.Bitmap(img_grey)

        #self.image = wx.StaticBitmap(self.panel, 1, self.bitmap_color)
        self.image = wx.BitmapButton(self.panel, 1, self.bitmap_color, style=wx.BORDER_NONE)
        # use 0 to not resize image to full window        
        self.hbox.Add(self.image, 0)

        # binds don't work on Linux for StaticBitmap
        # but they works for BitmapButton (but Button has border)
        self.image.Bind(wx.EVT_ENTER_WINDOW, self.OnOver)
        self.image.Bind(wx.EVT_LEAVE_WINDOW, self.OnLeave)

        # set color to see how many space use it
        self.panel.SetBackgroundColour((0,255,0))
        # set color to see how many space use it
        self.image.SetBackgroundColour((255,0,0))
        
    def OnOver(self, event):
        print('OnOver')
        self.image.SetBitmap(self.bitmap_grey)
        # update layout so it move image in correct place
        self.panel.Layout()

    def OnLeave(self, event):
        print('OnLeave')
        self.image.SetBitmap(self.bitmap_color)
        # update layout so it move image in correct place
        self.panel.Layout()


if __name__ == '__main__':
    app = wx.App()
    example = Example(None)
    example.Show()
    app.MainLoop()

