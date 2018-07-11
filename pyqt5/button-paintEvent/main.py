from PyQt5 import QtCore, QtGui, QtWidgets
import sys

class MyButton(QtWidgets.QPushButton):

    def paintEvent(self, event):
        qp = QtGui.QPainter()

        qp.begin(self)

        qp.setPen(QtGui.QColor(255, 0, 0))
        qp.setFont(QtGui.QFont('serif', 32))

        qp.drawText(event.rect(), QtCore.Qt.AlignCenter, 'Hello World')

        rect = event.rect() 
        for _ in range(9):
            rect.setX(rect.x() + 20)
            rect.setY(rect.y() + 20)
            rect.setWidth(rect.width() - 20)
            rect.setHeight(rect.height() - 20)
            qp.drawRect(rect)

        qp.end()        


class MyWindow(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        #self.setGeometry(0, 0, 300, 300)
        
        button1 = MyButton(self)
        button1.setMinimumSize(300, 300)
        button1.clicked.connect(self.on_click)
        
        button2 = MyButton(self)
        button2.setMinimumSize(300, 300)
        button2.clicked.connect(self.on_click)
        
        layout = QtWidgets.QHBoxLayout()
        layout.addWidget(button1)
        layout.addWidget(button2)

        self.setLayout(layout)

    def on_click(self, event):
        print('clicked')

if __name__ == '__main__':
    # Linux Mint 18.3 problem with style (GTK2/GTK3) 
    # "QApplication: invalid style override passed, ignoring it."
    sys.argv += ['-style', 'Fusion'] 
            
    app = QtWidgets.QApplication(sys.argv) #QApplication([]) #
    win = MyWindow()
    win.show()
    app.exec()
