
# date: 2019.08.26
# https://stackoverflow.com/questions/57656340/how-to-show-another-window

from PyQt5 import QtWidgets


class MainWidget(QtWidgets.QWidget):
    
    def __init__(self, parent):
        super().__init__()

        self.parent = parent
        
        self.button = QtWidgets.QPushButton("Show Second Window", self)
        self.button.clicked.connect(self.show_second_window)
        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(self.button)

        self.show()

    def show_second_window(self):
        self.close()
        self.parent.set_content("Second")


class SecondWidget(QtWidgets.QWidget):
    
    def __init__(self, parent):
        super().__init__()

        self.parent = parent
        
        self.button = QtWidgets.QPushButton("Close It", self)
        self.button.clicked.connect(self.show_second_window)
        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(self.button)

        self.show()

    def show_second_window(self):
        self.close()
        self.parent.set_content("Main")
    

class MainWindow(QtWidgets.QWidget):
    
    def __init__(self):
        super().__init__()

        self.layout = QtWidgets.QVBoxLayout(self)

        self.set_content("Main")

        self.show()

    def set_content(self, new_content):
        if new_content == "Main":
            self.content = MainWidget(self)
            self.layout.addWidget(self.content)
        elif new_content == "Second":           
            self.content = SecondWidget(self)
            self.layout.addWidget(self.content)


        
app = QtWidgets.QApplication([])
main = MainWindow()
app.exec()
