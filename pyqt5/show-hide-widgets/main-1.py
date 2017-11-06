#!/usr/bin/env python3

import sys
from PyQt5 import QtWidgets


class MainWidget(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.button = QtWidgets.QPushButton('Change widgets')
        self.button.clicked.connect(self.change_widgets)

        self.widget1 = QtWidgets.QLabel('Widget A')
        self.widget2 = QtWidgets.QLabel('Widget X')
        self.widget3 = QtWidgets.QLabel('Widget Y')
        
        self.widget2.hide()
        self.widget3.hide()

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.button)
        layout.addWidget(self.widget1)
        layout.addWidget(self.widget2)
        layout.addWidget(self.widget3)
        self.setLayout(layout)

        self.resize(320, 180)
        self.show()

    def change_widgets(self):
        if self.widget1.isHidden():
            self.widget1.show()
            self.widget2.hide()
            self.widget3.hide()
        else:
            self.widget1.hide()
            self.widget2.show()
            self.widget3.show()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    widget = MainWidget()
    app.exec()
