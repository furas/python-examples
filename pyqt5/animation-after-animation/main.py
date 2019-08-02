
# date: 2019.08.01
# https://stackoverflow.com/questions/57308598/rectangle-moving/57309451#57309451
# https://www.qtcentre.org/threads/32958-multiple-QPropertyAnimations-after-each-other-how
# https://doc.qt.io/qt-5/qpropertyanimation.html
# https://doc.qt.io/qt-5/qtimer.html
# https://doc.qt.io/qtforpython/PySide2/QtCore/QTimer.html

from PyQt5.QtWidgets import QWidget, QApplication, QFrame, QPushButton
from PyQt5.QtCore import QPropertyAnimation, QRect
from PyQt5.QtGui import QFont
import sys

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Animation Window")
        self.setGeometry(100, 100, 400, 400)
        self.widgets()
        self.show()

    def widgets(self):
        font = QFont("Times New Roman")
        font.setPixelSize(20)

        self.start = QPushButton("Start", self)
        self.start.setFont(font)
        self.start.setGeometry(100, 100, 100, 50)
        self.start.clicked.connect(self.doAnimation_1)

        self.frame = QFrame(self)
        self.frame.setStyleSheet("background-color:darkGreen;")
        self.frame.setFrameStyle(QFrame.Panel | QFrame.Raised)
        self.frame.setGeometry(250, 100, 100, 100)

    def doAnimation_1(self):
        self.anim = QPropertyAnimation(self.frame, b"geometry")
        self.anim.setDuration(1000)
        self.anim.setStartValue(QRect(0, 0, 100, 100))
        self.anim.setEndValue(QRect(300, 0, 100, 100))

        self.anim.finished.connect(self.doAnimation_2)
 
        self.anim.start()

    def doAnimation_2(self):
        self.anim = QPropertyAnimation(self.frame, b"geometry")
        self.anim.setDuration(1000)
        self.anim.setStartValue(QRect(300, 0, 100, 100))
        self.anim.setEndValue(QRect(300, 300, 100, 100))

        self.anim.finished.connect(self.doAnimation_3)
 
        self.anim.start()

    def doAnimation_3(self):
        self.anim = QPropertyAnimation(self.frame, b"geometry")
        self.anim.setDuration(1000)
        self.anim.setStartValue(QRect(300, 300, 100, 100))
        self.anim.setEndValue(QRect(0, 300, 100, 100))

        self.anim.finished.connect(self.doAnimation_4)
 
        self.anim.start()

    def doAnimation_4(self):
        self.anim = QPropertyAnimation(self.frame, b"geometry")
        self.anim.setDuration(1000)
        self.anim.setStartValue(QRect(0, 300, 100, 100))
        self.anim.setEndValue(QRect(0, 0, 100, 100))

        self.anim.finished.connect(self.doAnimation_1)
 
        self.anim.start()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
