#!/usr/bin/env python3

# https://pl.python.org/forum/index.php?topic=6010.msg25683#msg25683
import sys
from PyQt4 import QtGui, QtCore

# zmodyfikowany przyklad

class MyCanvas(QtGui.QWidget):
    
    def __init__(self):
        super(MyCanvas, self).__init__()

        self.selected_shape = 'rect'
        
        self.selected_pos = False
        self.selected_x1 = None
        self.selected_y1 = None
        self.selected_x2 = None
        self.selected_y2 = None
        
        self.shapes = []
        
    def paintEvent(self, event):

        qp = QtGui.QPainter()
        qp.begin(self)

        for name, args in self.shapes:
            
            if name == 'text':
                self.drawText(event, qp, args)
            elif name == 'rect':
                self.drawRect(event, qp, args)
            elif name == 'ellipse':
                self.drawEllipse(event, qp, args)

        if self.selected_pos:
            if self.selected_shape == 'rect':
                width = self.selected_x2 - self.selected_x1
                height = self.selected_y2 - self.selected_y1
                qp.drawRect(self.selected_x1, self.selected_y1, width, height)
            elif self.selected_shape == 'ellipse':
                width = abs(self.selected_x2 - self.selected_x1)
                height = abs(self.selected_y2 - self.selected_y1)
                x = self.selected_x1 - width
                y = self.selected_y1 - height
                width *= 2
                height *= 2
                qp.drawEllipse(x, y, width, height)
                
        qp.end()

    def drawRect(self, event, qp, args):
        qp.drawRect(args['x'], args['y'], args['width'], args['height'])
        
    def drawEllipse(self, event, qp, args):
        qp.drawEllipse(args['x']-args['width'], args['y']-args['height'], 2*args['width'], 2*args['height'])
        
    def drawText(self, event, qp, args):
      
        qp.setPen(QtGui.QColor(args['color']))
        qp.setFont(QtGui.QFont(args['font_name'], args['font_size']))
        
        qp.drawText(args['rect'], args['align'], args['text'])        
#        qp.drawText(args['rect'], QtCore.Qt.AlignCenter, self.text)        

    def mousePressEvent(self, event):
        #print('pressed:', event.button())

        if event.button() == 1:
            self.selected_pos = True
            self.selected_x1 = event.x()
            self.selected_y1 = event.y()
            
    def mouseReleaseEvent(self, event):
        #print('released:', event.button())
        
        if event.button() == 1 and self.selected_pos:
            self.selected_x2 = event.x()
            self.selected_y2 = event.y()
            self.selected_pos = False
            
            if self.selected_shape == 'text':
                #self.shapes.append(('text', {'x':event.x(), 'y':event.y(), 'r_x':20, 'r_y':20}))
                pass
            elif self.selected_shape == 'rect':
                x = min(self.selected_x1, self.selected_x2)
                y = min(self.selected_y1, self.selected_y2)
                width = abs(self.selected_x2 - self.selected_x1)
                height = abs(self.selected_y2 - self.selected_y1)
                self.shapes.append(('rect', {'x':x, 'y':y, 'width':width, 'height':height}))
                
            elif self.selected_shape == 'ellipse':
                width = abs(self.selected_x2 - self.selected_x1)
                height = abs(self.selected_y2 - self.selected_y1)
                x = self.selected_x1
                y = self.selected_y1
                self.shapes.append(('ellipse', {'x':x, 'y':y, 'width':width, 'height':height}))
            
        self.update()

    def mouseMoveEvent(self, event):
        if self.selected_pos:
            self.selected_x2 = event.x()
            self.selected_y2 = event.y()
            self.update()
            
# aplikacja

class App(QtGui.QWidget):

    def __init__(self):
        super(App, self).__init__()

        self.initUI()
        
    def initUI(self):      

        self.hboxlayout = QtGui.QHBoxLayout(self)
        self.setLayout(self.hboxlayout)
            
        self.A = MyCanvas()
        self.A.shapes.append(('rect', {'x':50, 'y':50, 'width':100, 'height':50}))

        self.B = MyCanvas()
        self.B.selected_shape = 'ellipse'


        self.hboxlayout.addWidget(self.A)
        self.hboxlayout.addWidget(self.B)

        self.setGeometry(300, 300, 600, 170)
        self.setWindowTitle('Dwa Płótna')
        self.show()
        
        
def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
