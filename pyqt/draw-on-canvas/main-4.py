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

        # biale tlo
        qp.fillRect(event.rect(), QtGui.QBrush(QtGui.QColor(255,255,255)))

        # rysowanie wszystkich figur
        for name, args in self.shapes:
            
            if name == 'rect':
                self.drawRect(event, qp, args)
            elif name == 'ellipse':
                self.drawEllipse(event, qp, args)
            elif name == 'triangle':
                self.drawTriangle(event, qp, args)

        # rysowanie "zaznaczenia"" podczas ciagniecia myszy
        if self.selection:
            args = {
                'x': self.selection_x1,
                'y': self.selection_y1,
                'width': self.selection_x2 - self.selection_x1,
                'height': self.selection_y2 - self.selection_y1,
            }
            
            if self.selection_shape == 'rect':
                self.drawRect(None, qp, args)
            elif self.selection_shape == 'ellipse':
                self.drawEllipse(None, qp, args)
            elif self.selection_shape == 'triangle':
                self.drawTriangle(None, qp, args)
                
        qp.end()

    def drawTriangle(self, event, qp, args):
        '''rysowanie trojkata'''
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
            # zapamietanie pozycji puszczenia
            self.selection_x2 = event.x()
            self.selection_y2 = event.y()
            self.selection = False

            # dane potrzebne do rysowania figury
            args = {
                'x': self.selection_x1,
                'y': self.selection_y1,
                'width': self.selection_x2 - self.selection_x1,
                'height': self.selection_y2 - self.selection_y1,
            }
            
            # dodawanie odpowiedniej figury do listy
            if self.selection_shape == 'rect':
                self.shapes.append(('rect', args))
                
            elif self.selection_shape == 'ellipse':
                self.shapes.append(('ellipse', args))

            elif self.selection_shape == 'triangle':
                self.shapes.append(('triangle', args))
            
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

        #--- plotno prostokaty ---

        # opis        
        self.labelRect = QtGui.QLabel(text="Rect:")
        self.vboxRect.addWidget(self.labelRect)

        # plotno
        self.canvasRect = MyCanvas()
        self.vboxRect.addWidget(self.canvasRect)

        # znaczek w rogu plotna
        self.canvasRect.shapes.append(('rect', {'x':5, 'y':5, 'width':20, 'height':20}))

        #--- elipsy ---
        
        # opis        
        self.labelEllipse = QtGui.QLabel(text="Ellipse:")
        self.vboxEllipse.addWidget(self.labelEllipse)

        # plotno
        self.canvasEllipse = MyCanvas()
        self.vboxEllipse.addWidget(self.canvasEllipse)

        # ustawienie rysowanego ksztaltu
        self.canvasEllipse.selection_shape = 'ellipse'

        # znaczek w rogu plotna
        self.canvasEllipse.shapes.append(('ellipse', {'x':5, 'y':5, 'width':20, 'height':20}))

        #--- trojkaty ---
        
        # opis        
        self.labelTriangle = QtGui.QLabel(text="Triangle:")
        self.vboxTriangle.addWidget(self.labelTriangle)

        # plotno
        self.canvasTriangle = MyCanvas()
        self.vboxTriangle.addWidget(self.canvasTriangle)

        # ustawienie rysowanego ksztaltu
        self.canvasTriangle.selection_shape = 'triangle'

        # znaczek w rogu plotna
        self.canvasTriangle.shapes.append(('triangle', {'x':5, 'y':5, 'width':20, 'height':20}))

        #---
        
        #self.setGeometry(300, 300, 600, 170)
        self.setWindowTitle('Trzy Płótna')
        self.show()

        
if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())

