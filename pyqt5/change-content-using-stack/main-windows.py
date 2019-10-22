
# date: 2019.08.26
# https://stackoverflow.com/questions/57656340/how-to-show-another-window

from PyQt5 import QtWidgets


class FirstWidget(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()

        layout = QtWidgets.QVBoxLayout(self)

        self.button = QtWidgets.QPushButton("Show Second", self)
        self.button.clicked.connect(self.show_other_window)

        layout.addWidget(self.button)

        self.show()

    def show_other_window(self):
        self.hide() # hide main window

        self.second = SecondWindow()
        self.second.exec() # will wait till you close second window

        self.show() # show main window again


class SecondWindow(QtWidgets.QDialog): # it has to be dialog

    def __init__(self):
        super().__init__()

        layout = QtWidgets.QVBoxLayout(self)

        self.button = QtWidgets.QPushButton("Close It", self)
        self.button.clicked.connect(self.show_other_window)

        layout.addWidget(self.button)

        self.show()

    def show_other_window(self):
        self.close() # go back to main window


app = QtWidgets.QApplication([])
main = MainWindow()
app.exec()
