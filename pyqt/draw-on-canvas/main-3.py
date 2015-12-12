#!/usr/bin/env python3

# http://zetcode.com/gui/pyqt4/drawing/
# https://pl.python.org/forum/index.php?topic=6010.msg25683#msg25683

import sys
from PyQt4 import QtGui, QtCore

# --- płótno ---

class MyCanvas(QtGui.QWidget):
    
    def __init__(self):
        super(MyCanvas, self).__init__()

        # domyslan wielkosc
        self.setFixedSize(400, 400)

        # rysowana figura
        self.selection_shape = 'rect'

        # pozycja poczatkowa i koncowa podczas rysowania "zaznaczenia"
        self.selection = False
        self.selection_x1 = None
        self.selection_y1 = None
        self.selection_x2 = None
        self.selection_y2 = None

        # lista figur do rysowania
        self.shapes = []
        
    def paintEvent(self, event):

        qp = QtGui.QPainter()
        qp.begin(self)

        # rysowanie ramki - trzeba zmniejszyc dlugosc i szerokosc o jeden
        #~ rect = event.rect()
        #~ rect.setWidth(rect.width()-1)
        #~ rect.setHeight(rect.height()-1)
        #~ qp.drawRect(rect)

        # biale tło
        qp.fillRect(event.rect(), QtGui.QBrush(QtGui.QColor(255,255,255)))

        # rysowanie wszystkich figur
        for name, args in self.shapes:
            
            if name == 'text':
                self.drawText(event, qp, args)
            elif name == 'rect':
                self.drawRect(event, qp, args)
            elif name == 'ellipse':
                self.drawEllipse(event, qp, args)
            elif name == 'triangle':
                self.drawTriangle(event, qp, args)

        # rysowanie "zaznaczenia"" podczas ciagniecia myszy
        if self.selection:
            width = self.selection_x2 - self.selection_x1
            height = self.selection_y2 - self.selection_y1
            
            if self.selection_shape == 'rect':
                qp.drawRect(self.selection_x1, self.selection_y1, width, height)
                
            elif self.selection_shape == 'ellipse':
                qp.drawEllipse(self.selection_x1, self.selection_y1, width, height)
                
            elif self.selection_shape == 'triangle':
                args = {
                    'x': self.selection_x1,
                    'y': self.selection_y1,
                    'width': width,
                    'height': height,
                }
                self.drawTriangle(None, qp, args)
                
        qp.end()

    def drawTriangle(self, event, qp, args):
        '''rysowanie prostokata'''
        x1 = args['x']
        y1 = args['y']+args['height']
        x2 = args['x']+args['width']
        y2 = y1
        x3 = x1+(args['width']/2)
        y3 = args['y']
        qp.drawLine(x1, y1, x2, y2)
        qp.drawLine(x1, y1, x3, y3)
        qp.drawLine(x2, y2, x3, y3)
        
    def drawRect(self, event, qp, args):
        '''rysowanie prostokata'''
        qp.drawRect(args['x'], args['y'], args['width'], args['height'])
        
    def drawEllipse(self, event, qp, args):
        '''rysowanie elipsy'''
        qp.drawEllipse(args['x'], args['y'], args['width'], args['height'])
       
    def drawText(self, event, qp, args):
        '''rysowanie tekstu'''
        qp.setPen(QtGui.QColor(args['color']))
        qp.setFont(QtGui.QFont(args['font_name'], args['font_size']))
        
        qp.drawText(args['rect'], args['align'], args['text'])        
        #qp.drawText(args['rect'], QtCore.Qt.AlignCenter, self.text)        

    def mousePressEvent(self, event):
        #print('pressed:', event.button())

        # zapamietanie wcisnietego przycisku
        if event.button() == 1:
            self.selection = True
            self.selection_x1 = event.x()
            self.selection_y1 = event.y()
            
    def mouseReleaseEvent(self, event):
        #print('released:', event.button())

        # puszczanie przycisku 
        if event.button() == 1 and self.selection:
            self.selection_x2 = event.x()
            self.selection_y2 = event.y()
            self.selection = False

            # nie działa z trójkątem
            #~ x = min(self.selection_x1, self.selection_x2)
            #~ y = min(self.selection_y1, self.selection_y2)
            #~ width = abs(self.selection_x2 - self.selection_x1)
            #~ height = abs(self.selection_y2 - self.selection_y1)

            x = self.selection_x1
            y = self.selection_y1
            width = self.selection_x2 - self.selection_x1
            height = self.selection_y2 - self.selection_y1

            # dodawanie odpowiedniej figury do listy
            if self.selection_shape == 'text':
                #self.shapes.append(('text', {'x':event.x(), 'y':event.y(), 'r_x':20, 'r_y':20}))
                pass

            elif self.selection_shape == 'rect':
                self.shapes.append(('rect', {'x':x, 'y':y, 'width':width, 'height':height}))
                
            elif self.selection_shape == 'ellipse':
                self.shapes.append(('ellipse', {'x':x, 'y':y, 'width':width, 'height':height}))

            elif self.selection_shape == 'triangle':
                self.shapes.append(('triangle', {'x':x, 'y':y, 'width':width, 'height':height}))
            
        self.update()

    def mouseMoveEvent(self, event):
        # zapamietanie pozycji myszki przy przycisnietym przycisku
        # i odswiezenie ekranu
        if self.selection:
            self.selection_x2 = event.x()
            self.selection_y2 = event.y()
            self.update()
            

# --- Aplikacja ---

class App(QtGui.QWidget):

    def __init__(self):
        super(App, self).__init__()

        self.initUI()
        
    def initUI(self):      

        self.hboxlayout = QtGui.QHBoxLayout(self)
        self.setLayout(self.hboxlayout)

        self.vboxRect = QtGui.QVBoxLayout()
        self.vboxEllipse = QtGui.QVBoxLayout()
        self.vboxTriangle = QtGui.QVBoxLayout()
        self.hboxlayout.addLayout(self.vboxRect)
        self.hboxlayout.addLayout(self.vboxEllipse)
        self.hboxlayout.addLayout(self.vboxTriangle)

        #---
        
        self.labelRect = QtGui.QLabel(text="Rect:")
        self.vboxRect.addWidget(self.labelRect)
        
        self.canvasRect = MyCanvas()
        self.vboxRect.addWidget(self.canvasRect)

        self.canvasRect.shapes.append(('rect', {'x':5, 'y':5, 'width':20, 'height':20}))

        #---
        
        self.labelEllipse = QtGui.QLabel(text="Ellipse:")
        self.vboxEllipse.addWidget(self.labelEllipse)

        self.canvasEllipse = MyCanvas()
        self.vboxEllipse.addWidget(self.canvasEllipse)

        self.canvasEllipse.selection_shape = 'ellipse'

        self.canvasEllipse.shapes.append(('ellipse', {'x':5, 'y':5, 'width':20, 'height':20}))

        #---
        
        self.labelTriangle = QtGui.QLabel(text="Triangle:")
        self.vboxTriangle.addWidget(self.labelTriangle)

        self.canvasTriangle = MyCanvas()
        self.vboxTriangle.addWidget(self.canvasTriangle)

        self.canvasTriangle.selection_shape = 'triangle'

        self.canvasTriangle.shapes.append(('triangle', {'x':5, 'y':5, 'width':20, 'height':20}))

        #---
        
        #self.setGeometry(300, 300, 600, 170)
        self.setWindowTitle('Trzy Płótna')
        self.show()

        
if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())

