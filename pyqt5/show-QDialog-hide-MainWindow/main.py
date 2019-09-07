
# date: 2019.08.26
# https://stackoverflow.com/questions/57656340/how-to-show-another-window

from PyQt5 import QtWidgets
import sys

class MainWindow(QtWidgets.QWidget):
    
    def __init__(self):
        super().__init__()

        self.button = QtWidgets.QPushButton("Show Second", self)
        self.button.clicked.connect(self.show_second_window)
        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(self.button)

        self.show()

    def show_second_window(self):
        self.hide() # hide main window
        
        self.second = SecondWindow()
        self.second.exec() # will wait till you close second window
        
        self.show() # show main window again


class SecondWindow(QtWidgets.QDialog): # it has to be dialog
    
    def __init__(self):
        super().__init__()

        self.button = QtWidgets.QPushButton("Close Second", self)
        self.button.clicked.connect(self.show_second_window)
        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(self.button)

        self.show()

    def show_second_window(self):
        self.close() # go back to main window
    
        
#app = QtWidgets.QApplication([])
app = QtWidgets.QApplication(sys.argv)
main = MainWindow()
app.exec()
