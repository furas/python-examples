
# date: 2019.08.15
# https://stackoverflow.com/questions/57503168/add-delete-plots-independently-on-a-matplotlib-figure/57503316#57503316

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.pyplot import Figure

class Mainwindow(QMainWindow):
    def __init__(self, parent=None):
        super(Mainwindow, self).__init__(parent)

        centralWidget = QWidget()
        self.setCentralWidget(centralWidget)
        self.fig = Figure()
        self.axes = self.fig.add_subplot(111)
        self.canvas = FigureCanvas(self.fig)
        self.gridLayout = QGridLayout(centralWidget)
        self.gridLayout.addWidget(self.canvas)   
        self.btn_plot = QCheckBox("Plot")
        self.btn_line = QCheckBox("Line")
        self.gridLayout.addWidget(self.btn_plot, 1,0,1,1)
        self.gridLayout.addWidget(self.btn_line, 2,0,1,1)
        self.btn_plot.clicked.connect(self.btnPlot)
        self.btn_line.clicked.connect(self.btnLine)

        self.Graphics = Graphics(self.axes)

    def btnPlot(self):
        self.Graphics.drawPlot(self.btn_plot.isChecked())
        
    def btnLine(self):
        self.Graphics.drawLine(self.btn_line.isChecked())

class Graphics:
    def __init__(self, axes):
        self.axes = axes
        # create at start with default values
        self.plot = None
        self.vline1 = None
        self.vline2 = None
        
    def drawPlot(self, checked):
        if checked:
            self.plot = self.axes.plot([10,20,30], [5,10,2], 'o')
        else:
            for item in self.plot:
                item.remove()
        self.axes.figure.canvas.draw()

    def drawLine(self, checked):
        if checked:
            self.vline1 = self.axes.axvline(x=15, linestyle="dashed", color="#595959")
            self.vline2 = self.axes.axvline(x=25, linestyle="dashed", color="#595959")
        else:
            self.vline1.remove()
            self.vline2.remove()
        self.axes.figure.canvas.draw()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    prog = Mainwindow()   
    prog.show()
    sys.exit(app.exec_())
