#!/usr/bin/env python3

from PyQt5 import QtCore, QtGui, QtWidgets
import sys


class MyRect(QtWidgets.QGraphicsRectItem):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.setRect(50, 50, 50, 50)

    def mousePressEvent(self, event):
        print('press')

        # left - start dragging
        if event.button() == QtCore.Qt.LeftButton: # value 1
            print('left')

        # right - close application
        if event.button() == QtCore.Qt.RightButton: # value 2
            self.close()

        # middle - something different
        if event.button() == QtCore.Qt.MiddleButton: # value 4
            print('middle')

    def mouseMoveEvent(self, event):
        print('move')
    
    def mouseReleaseEvent(self, event):
        print('release')



class MyWindow(QtWidgets.QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.view = QtWidgets.QGraphicsView()
        self.scene = QtWidgets.QGraphicsScene(self)
        self.view.setScene(self.scene)

        my_rect = MyRect()

        self.scene.addItem(my_rect)

        layout = QtWidgets.QHBoxLayout()
        layout.addWidget(self.view)
        self.setLayout(layout)


if __name__ == '__main__':
    # Linux Mint 18.3 problem with style (GTK2/GTK3) 
    # "QApplication: invalid style override passed, ignoring it."
    sys.argv += ['-style', 'Fusion'] 
            
    app = QtWidgets.QApplication(sys.argv) #QApplication([]) #
    win = MyWindow()
    win.show()
    app.exec()
