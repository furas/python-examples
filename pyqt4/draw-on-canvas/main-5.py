#!/usr/bin/env python3

# http://zetcode.com/gui/pyqt4/drawing/
# https://pl.python.org/forum/index.php?topic=6010.msg25683#msg25683

import sys
from PyQt4 import QtGui, QtCore, Qt

# --- płótno ---

class MyCanvas(QtGui.QWidget):
    
    def __init__(self):
        super(MyCanvas, self).__init__()

        # domyslan wielkosc
        self.setFixedSize(400, 400)

        # rysowana figura
        self.selection_shape = 'rect'
        self.selection_color = 'black'
        self.selection_fill  = None

        # pozycja poczatkowa i koncowa podczas rysowania "zaznaczenia"
        self.selection = False
        self.selection_x1 = None
        self.selection_y1 = None
        self.selection_x2 = None
        self.selection_y2 = None

        # lista figur do rysowania
        self.shapes = []

    def setShape(self, shape):
        self.selection_shape = shape
        
    def setColor(self, color):
        self.selection_color = color
        
    def setFill(self, fill):
        self.selection_fill = fill
        
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
                'color': 'black',
                'fill': None,
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

        if args['color']:
            qp.setPen(QtGui.QColor(args['color']))
            
        if args['fill']:
            qp.setBrush(QtGui.QColor(args['fill']))
        else:
            qp.setBrush(QtCore.Qt.NoBrush)
            
        qp.drawLine(x1, y1, x2, y2)
        qp.drawLine(x1, y1, x3, y3)
        qp.drawLine(x2, y2, x3, y3)
        
    def drawRect(self, event, qp, args):
        '''rysowanie prostokata'''
        if args['color']:
            qp.setPen(QtGui.QColor(args['color']))
            
        if args['fill']:
            qp.setBrush(QtGui.QColor(args['fill']))
        else:
            qp.setBrush(QtCore.Qt.NoBrush)
            
        qp.drawRect(args['x'], args['y'], args['width'], args['height'])
        
    def drawEllipse(self, event, qp, args):
        '''rysowanie elipsy'''
        if args['color']:
            qp.setPen(QtGui.QColor(args['color']))
            
        if args['fill']:
            qp.setBrush(QtGui.QColor(args['fill']))
        else:
            qp.setBrush(QtCore.Qt.NoBrush)
            
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
                'color': self.selection_color,
                'fill': self.selection_fill,
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

        self.vbox = QtGui.QVBoxLayout(self)
        self.setLayout(self.vbox)

        #--- narzedzia ---
        
        self.hboxTools = QtGui.QHBoxLayout()
        self.vbox.addLayout(self.hboxTools)

        self.buttonShapeRect = QtGui.QPushButton("Rectangle", self)
        #self.buttonShapeRect.setCheckable(True)
        self.buttonShapeRect.clicked.connect(lambda:self.canvas.setShape('rect'))
        self.hboxTools.addWidget(self.buttonShapeRect)
        
        self.buttonShapeEllipse = QtGui.QPushButton("Ellipse", self)
        #self.buttonShapeEllipse.setCheckable(True)
        self.buttonShapeEllipse.clicked.connect(lambda:self.canvas.setShape('ellipse'))
        self.hboxTools.addWidget(self.buttonShapeEllipse)
        
        self.buttonShapeTriangle = QtGui.QPushButton("Triangle", self)
        #self.buttonShapeTriangle.setCheckable(True)
        self.buttonShapeTriangle.clicked.connect(lambda:self.canvas.setShape('triangle'))
        self.hboxTools.addWidget(self.buttonShapeTriangle)
        
        #--- plotno ---

        self.canvas = MyCanvas()
        self.vbox.addWidget(self.canvas)

        #--- kolory ----

        self.hboxColors = QtGui.QHBoxLayout()
        self.vbox.addLayout(self.hboxColors)

        self.buttonColorRed = QtGui.QPushButton("Red", self)
        self.buttonColorRed.clicked.connect(lambda:self.canvas.setColor('red'))
        self.hboxColors.addWidget(self.buttonColorRed)
        
        self.buttonColorGreen = QtGui.QPushButton("Green", self)
        #self.buttonColorEllipse.setCheckable(True)
        self.buttonColorGreen.clicked.connect(lambda:self.canvas.setColor('green'))
        self.hboxColors.addWidget(self.buttonColorGreen)
        
        self.buttonColorBlue = QtGui.QPushButton("Blue", self)
        #self.buttonColorTriangle.setCheckable(True)
        self.buttonColorBlue.clicked.connect(lambda:self.canvas.setColor('blue'))
        self.hboxColors.addWidget(self.buttonColorBlue)
        
        #--- wypelnienia ----

        self.hboxFills = QtGui.QHBoxLayout()
        self.vbox.addLayout(self.hboxFills)

        self.buttonFillRed = QtGui.QPushButton("Red", self)
        self.buttonFillRed.clicked.connect(lambda:self.canvas.setFill('red'))
        self.hboxFills.addWidget(self.buttonFillRed)
        
        self.buttonFillGreen = QtGui.QPushButton("Green", self)
        #self.buttonFillEllipse.setCheckable(True)
        self.buttonFillGreen.clicked.connect(lambda:self.canvas.setFill('green'))
        self.hboxFills.addWidget(self.buttonFillGreen)
        
        self.buttonFillBlue = QtGui.QPushButton("Blue", self)
        #self.buttonFillTriangle.setCheckable(True)
        self.buttonFillBlue.clicked.connect(lambda:self.canvas.setFill('blue'))
        self.hboxFills.addWidget(self.buttonFillBlue)
        
        #---
        
        #self.setGeometry(300, 300, 600, 170)
        self.setWindowTitle('Trzy Płótna')
        self.show()

        
if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())

