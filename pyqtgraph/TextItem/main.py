from PyQt5 import QtGui
import pyqtgraph as pg

app = QtGui.QApplication([])

x = [1,2,3,4,5]
y = [0,3,1,2,0]

plotWidget = pg.plot()
plotWidget.plot(x, y)
    
text = pg.TextItem("Hello World", color='f00')
plotWidget.addItem(text)
text.setPos(3, 2)
    
app.exec_()
