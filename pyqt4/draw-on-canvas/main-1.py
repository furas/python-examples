#!/usr/bin/env python3

# http://zetcode.com/gui/pyqt4/drawing/
# https://pl.python.org/forum/index.php?topic=6010.msg25683#msg25683

import sys
from PyQt4 import QtGui, QtCore

# zmodyfikowany przyklad

class MyCanvas(QtGui.QWidget):
    
    def __init__(self):
        super(MyCanvas, self).__init__()
        
        self.initUI()
        
    def initUI(self):      

        self.text = u'\u041b\u0435\u0432 \u041d\u0438\u043a\u043e\u043b\u0430\
\u0435\u0432\u0438\u0447 \u0422\u043e\u043b\u0441\u0442\u043e\u0439: \n\
\u0410\u043d\u043d\u0430 \u041a\u0430\u0440\u0435\u043d\u0438\u043d\u0430'

#        self.setGeometry(300, 300, 280, 170)
#        self.setWindowTitle('Draw text')
#        self.show()

        self.shapes = []
        
        for x in range(0, 280, 20):
            self.shapes.append( ('kwadrat', (x, 0, 20, 20)) )

        for x in range(5, 280, 20):
            self.shapes.append( ('okrag', (x, 5, 10, 10)) )

    def paintEvent(self, event):

        qp = QtGui.QPainter()
        qp.begin(self)
        self.drawText(event, qp)

        for name, info in self.shapes:
            if name == 'kwadrat':
                qp.drawRect(*info)
            elif name == 'okrag':
                qp.drawEllipse(*info)

        qp.end()
        
    def drawText(self, event, qp):
      
        qp.setPen(QtGui.QColor(168, 34, 3))
        qp.setFont(QtGui.QFont('Decorative', 10))
        qp.drawText(event.rect(), QtCore.Qt.AlignCenter, self.text)        

    def mousePressEvent(self, event):
        self.shapes.append(('okrag', (event.x()-10, event.y()-10, 20, 20)))
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
        self.B = MyCanvas()

        self.A.shapes.append(('kwadrat', (50, 50, 190, 50)))

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
