#!/usr/bin/env python3

# http://zetcode.com/gui/pyqt4/drawing/
# https://pl.python.org/forum/index.php?topic=6010.msg25683#msg25683

# maybe better to use QGraphicsView, QGraphicsScene, QGraphicsItem

import sys
from PyQt4 import QtGui, QtCore

# --- canvas ---

class MyCanvas(QtGui.QWidget):
    
    def __init__(self):
        super(MyCanvas, self).__init__()

        # default size
        self.setFixedSize(600, 400)

        # drawed "selection"
        self.selection_shape = 'rect'
        self.selection_color = 'black'
        self.selection_fill  = None

        self.selection = False
        self.selection_x1 = None
        self.selection_y1 = None
        self.selection_x2 = None
        self.selection_y2 = None

        # list with shapes
        self.shapes = []

        self.pallete = [ #(button text, color)
            ('None', None),
            ('Black', 'black'), # QtCore.Qt.black
            ('Red', 'red'),     # QtCore.Qt.red
            ('Green', 'green'), # QtCore.Qt.green
            ('Blue', 'blue'),   # QtCore.Qt.blue
        ]

        self.tools = [ # (button name, shape)
            ('Rectangle', 'rect'),
            ('Ellipse', 'ellipse'),
            ('Triangle', 'triangle'),
            ('Hexagon', 'hexagon'),
        ]

    def setShape(self, shape):
        print('shape:', shape)
        self.selection_shape = shape
        
    def setColor(self, color):
        print('color:', color)
        self.selection_color = color
        
    def setFill(self, fill):
        print('fill:', fill)
        self.selection_fill = fill
        
    def paintEvent(self, event):

        qp = QtGui.QPainter()
        qp.begin(self)

        # white background
        qp.fillRect(event.rect(), QtGui.QBrush(QtGui.QColor(255,255,255)))

        # drawing shapes from list
        for name, args in self.shapes:
            if name == 'rect':
                self.drawRect(event, qp, args)
            elif name == 'ellipse':
                self.drawEllipse(event, qp, args)
            elif name == 'triangle':
                self.drawTriangle(event, qp, args)
            elif name == 'hexagon':
                self.drawHexagon(event, qp, args)

        # drawing "selection" during mouse move
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
            elif self.selection_shape == 'hexagon':
                self.drawHexagon(None, qp, args)
                
        qp.end()

    def drawRect(self, event, qp, args):
        '''drawing rectangle'''

        # change border color
        if args['color']:
            qp.setPen(QtGui.QColor(args['color']))
        else:
            qp.setPen(QtCore.Qt.NoPen)

        # change fill color
        if args['fill']:
            qp.setBrush(QtGui.QColor(args['fill']))
        else:
            qp.setBrush(QtCore.Qt.NoBrush)

        # draw
        qp.drawRect(args['x'], args['y'], args['width'], args['height'])
        
    def drawEllipse(self, event, qp, args):
        '''drawing ellipse'''

        # change border color
        if args['color']:
            qp.setPen(QtGui.QColor(args['color']))
        else:
            qp.setPen(QtCore.Qt.NoPen)
            
        if args['fill']:
            qp.setBrush(QtGui.QColor(args['fill']))
        else:
            qp.setBrush(QtCore.Qt.NoBrush)
            
        # draw
        qp.drawEllipse(args['x'], args['y'], args['width'], args['height'])

    def drawTriangle(self, event, qp, args):
        '''drawing rectangle'''

        # change border color
        if args['color']:
            qp.setPen(QtGui.QColor(args['color']))
        else:
            qp.setPen(QtCore.Qt.NoPen)
            
        # change fill color
        if args['fill']:
            qp.setBrush(QtGui.QColor(args['fill']))
        else:
            qp.setBrush(QtCore.Qt.NoBrush)

        # create polygon
        
        x1 = args['x']
        y1 = args['y']+args['height']
        x2 = args['x']+args['width']
        y2 = y1
        x3 = x1+(args['width']/2)
        y3 = args['y']

        points = QtGui.QPolygon([
            QtCore.QPoint(x1, y1),
            QtCore.QPoint(x2, y2),
            QtCore.QPoint(x3, y3),
            QtCore.QPoint(x1, y1)
        ])        

        # draw
        qp.drawPolygon(points)
        
    def drawHexagon(self, event, qp, args):
        '''drawing star'''

        # change border color
        if args['color']:
            qp.setPen(QtGui.QColor(args['color']))
        else:
            qp.setPen(QtCore.Qt.NoPen)
            
        # change fill color
        if args['fill']:
            qp.setBrush(QtGui.QColor(args['fill']))
        else:
            qp.setBrush(QtCore.Qt.NoBrush)

        # create polygon
        
        x1 = args['x']
        y1 = args['y'] + 1/2 * args['height']
        
        x2 = args['x'] + 1/4 * args['width']
        y2 = args['y']
        
        x3 = args['x'] + 3/4 * args['width']
        y3 = args['y'] 

        x4 = args['x'] + args['width']
        y4 = args['y'] + 1/2 * args['height']
        
        x5 = args['x'] + 3/4 * args['width']
        y5 = args['y'] + args['height']
        
        x6 = args['x'] + 1/4 * args['width']
        y6 = args['y'] + args['height']

        points = QtGui.QPolygon([
            QtCore.QPoint(x1, y1),
            QtCore.QPoint(x2, y2),
            QtCore.QPoint(x3, y3),
            QtCore.QPoint(x4, y4),
            QtCore.QPoint(x5, y5),
            QtCore.QPoint(x6, y6),
            QtCore.QPoint(x1, y1),
        ])        

        # draw
        qp.drawPolygon(points)
        
    def mousePressEvent(self, event):
        #print('pressed:', event.button())

        # remember press position
        if event.button() == 1:
            self.selection = True
            self.selection_x1 = event.x()
            self.selection_y1 = event.y()
            
    def mouseReleaseEvent(self, event):
        #print('released:', event.button())

        # remember releas position
        if event.button() == 1 and self.selection:
            self.selection_x2 = event.x()
            self.selection_y2 = event.y()
            self.selection = False

            # args to add shape to list
            args = {
                'x': self.selection_x1,
                'y': self.selection_y1,
                'width': self.selection_x2 - self.selection_x1,
                'height': self.selection_y2 - self.selection_y1,
                'color': self.selection_color,
                'fill': self.selection_fill,
            }
            
            # add shape to list
            self.shapes.append((self.selection_shape, args))
            
        self.update()

    def mouseMoveEvent(self, event):
        # remember mouse position to refresh "selection"
        if self.selection:
            self.selection_x2 = event.x()
            self.selection_y2 = event.y()
            self.update()
            

# --- main ---

class App(QtGui.QWidget):

    def __init__(self):
        super(App, self).__init__()

        self.initUI()
        
    def initUI(self):      

        self.vbox = QtGui.QVBoxLayout(self)
        self.setLayout(self.vbox)

        #--- canvas - created to get tool list ---
        
        self.canvas = MyCanvas()

        #--- tool buttons ---
        
        self.hboxTools = QtGui.QHBoxLayout()

        for name, shape in self.canvas.tools:
            btn = QtGui.QPushButton(name)
            btn.setCheckable(True)
            btn.setAutoExclusive(True)            
            btn.clicked.connect(lambda x,s=shape:self.canvas.setShape(s))
            self.hboxTools.addWidget(btn)

            if name == 'Rectangle':
                btn.setChecked(True)
        
        self.btnToolsGroup = QtGui.QGroupBox("Tool")
        self.btnToolsGroup.setLayout(self.hboxTools)
        self.vbox.addWidget(self.btnToolsGroup)
        
        #--- canvas - add to window ---

        self.vbox.addWidget(self.canvas)

        #--- color buttons ----

        self.hboxColors = QtGui.QHBoxLayout()

        for name, color in self.canvas.pallete:
            
            btn = QtGui.QPushButton(name, self)
            btn.setCheckable(True)
            btn.setAutoExclusive(True)            
            btn.clicked.connect(lambda x,c=color:self.canvas.setColor(c))
            self.hboxColors.addWidget(btn)

            if name == 'Black':
                btn.setChecked(True)

        self.btnColorsGroup = QtGui.QGroupBox("Border")
        self.btnColorsGroup.setLayout(self.hboxColors)
        self.vbox.addWidget(self.btnColorsGroup)
        
        #--- fill buttons ----

        self.hboxFills = QtGui.QHBoxLayout()

        for name, color in self.canvas.pallete:
            
            btn = QtGui.QPushButton(name, self)
            btn.setCheckable(True)
            btn.setAutoExclusive(True)
            btn.clicked.connect(lambda x,c=color:self.canvas.setFill(c))
            self.hboxFills.addWidget(btn)

            if name == 'None':
                btn.setChecked(True)

        self.btnFillsGroup = QtGui.QGroupBox("Fill")
        self.btnFillsGroup.setLayout(self.hboxFills)        
        self.vbox.addWidget(self.btnFillsGroup)
        
        #---
        
        #self.setGeometry(300, 300, 600, 170)
        self.setWindowTitle('MyCanvas')
        self.show()

        
if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
