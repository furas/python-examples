from PyQt5 import QtCore, QtGui, QtWidgets
import sys

class MyWindow(QtWidgets.QWidget):
    
    relative_x = None
    relative_y = None
    drag = None
    
    def mouseReleaseEvent(self, event):
        if event.button() == 1: # left
            self.drag = False
        
    def mousePressEvent(self, event):
        if event.button() == 1: # left
            self.drag = True
            # mouse position
            point = event.screenPos()
            # window position
            rect = self.geometry()
        
            # distance between both
            self.relative_x = point.x() - rect.x()
            self.relative_y = point.y() - rect.y()

        if event.button() == 2: # right
            self.close()

        if event.button() == 4: # middle
            print('middle')

    def mouseMoveEvent(self, event):
        if self.drag:
            # mouse position
            point = event.screenPos()
            # window new position
            new_x = point.x() - self.relative_x
            new_y = point.y() - self.relative_y
            self.move(new_x, new_y)
            
# Linux Mint 18.3 problem with style (GTK2/GTK3) 
# "QApplication: invalid style override passed, ignoring it."
#sys.argv += ['--style', 'Fusion'] 
        
app = QtWidgets.QApplication(sys.argv) #QApplication([]) #

win = MyWindow()
# transparent window but with frame/border
#win.setAttribute(QtCore.Qt.WA_TranslucentBackground)
# remove frame/border 
win.setWindowFlags(QtCore.Qt.FramelessWindowHint)

win.show()

app.exec()
