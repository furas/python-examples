from PyQt5 import QtCore, QtGui, QtWidgets
import sys

class MyWindow(QtWidgets.QWidget):
    
    relative_x = None
    relative_y = None
    drag = None
    
    def mousePressEvent(self, event):
        # left - start dragging
        if event.button() == 1: # left
            self.drag = True
            
            # mouse start position on screeen
            point = event.screenPos()
            
            # window start position on screen
            rect = self.geometry()
        
            # distance between mouse and left, top corner of window
            self.relative_x = point.x() - rect.x()
            self.relative_y = point.y() - rect.y()

        # right - close application
        if event.button() == 2: # right
            self.close()

        # middle - something different
        if event.button() == 4: # middle
            print('middle')

    def mouseMoveEvent(self, event):
        # drag window
        if self.drag:
            # mouse current position on screen
            point = event.screenPos()
            
            # calculate window new position on screen
            new_x = point.x() - self.relative_x
            new_y = point.y() - self.relative_y
            
            # move window
            self.move(new_x, new_y)

    def mouseReleaseEvent(self, event):
        # stop dragging
        if event.button() == 1: # left
            self.drag = False


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
