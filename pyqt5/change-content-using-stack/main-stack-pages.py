
# date: 2019.08.26
# https://stackoverflow.com/questions/57656340/how-to-show-another-window

# change content with QStackedLayout

from PyQt5 import QtWidgets


class FirstWidget(QtWidgets.QWidget):

    def __init__(self, parent):
        super().__init__(parent=parent)

        layout = QtWidgets.QVBoxLayout(self)

        self.button = QtWidgets.QPushButton("Show Second", self)
        self.button.clicked.connect(self.show_other_page)

        layout.addWidget(self.button)

    def show_other_page(self):
        self.parent().stack.setCurrentIndex(1)


class SecondWidget(QtWidgets.QWidget):

    def __init__(self, parent):
        super().__init__(parent=parent)

        layout = QtWidgets.QVBoxLayout(self)

        self.button = QtWidgets.QPushButton("Show First", self)
        self.button.clicked.connect(self.show_other_page)

        layout.addWidget(self.button)

    def show_other_page(self):
        self.parent().stack.setCurrentIndex(0)


class MainWindow(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()

        self.stack = QtWidgets.QStackedLayout(self)

        self.stack1 = FirstWidget(self)
        self.stack2 = SecondWidget(self)

        self.stack.addWidget(self.stack1)
        self.stack.addWidget(self.stack2)
        
        self.show()


app = QtWidgets.QApplication([])
main = MainWindow()
app.exec()
