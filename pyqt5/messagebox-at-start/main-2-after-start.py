#!/usr/bin/env python3

# date: 2019.08.13
# https://stackoverflow.com/questions/57482730/is-there-a-way-to-show-a-pyqt5-qmessagebox-at-the-start-of-the-program-without-i

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox

# --- classes ---

class MyApp(QWidget):

    def __init__(self):
        super().__init__()

        self.show() # show main window

        self.show_message() # show message

    def show_message(self):
        msg = QMessageBox()
        msg.setWindowTitle('Initial information')
        msg.setText("Please use the 'Close (F6)' button to close the program.\n\n"
                    "Closing it by pressing the red X button on the top will "
                    "leave the autoclicker running until the key 'F6' is pressed.")
        msg.setIcon(QMessageBox.Information)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec()

# --- functions ---

# --- main ---

app = QApplication([])

my_app = MyApp()

app.exec()
