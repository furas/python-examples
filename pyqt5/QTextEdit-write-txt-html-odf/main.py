#!/usr/bin/env python3

from PyQt5 import QtCore, QtGui, QtWidgets
import sys


class MyWindow(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()

        self.editor = QtWidgets.QTextEdit(self)
        self.editor.insertHtml('<b>bold text</b><br><i>italic text</i><br><ul><li>One<\li><li>One<\li></ul>')

        button = QtWidgets.QPushButton(self, text='WRITE')
        button.clicked.connect(self.on_click)
        
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.editor)
        layout.addWidget(button)

        self.setLayout(layout)


    def on_click(self, event):
        #print(self.editor.toPlainText())
        #print(self.editor.toHtml())

        # https://doc.qt.io/qt-5/qtextdocumentwriter.html
        #writer = QtGui.QTextDocumentWriter('output.odf')
        writer = QtGui.QTextDocumentWriter()

        for item in writer.supportedDocumentFormats():
            print('format:', bytes(item).decode())

        doc = self.editor.document()

        writer.setFormat(b'ODF') # has to be bytes, not string
        writer.setFileName('output.odf')
        writer.write(doc)

        writer.setFormat(b'HTML') # has to be bytes, not string
        writer.setFileName('output.html')
        writer.write(doc)
        
        writer.setFormat(b'plaintext') # has to be bytes, not string
        writer.setFileName('output.txt')
        writer.write(doc)

        printer = QPrinter()
        printer.setOutputFormat(QPrinter.PdfFormat)
        printer.setPaperSize(QPrinter.A4);
        printer.setOutputFileName('output.pdf')
        #doc.setPageSize(printer.pageRect().size()) # need QSizeF instead of QSize
        doc.print(printer)
        

if __name__ == '__main__':
    # Linux Mint 18.3 problem with style (GTK2/GTK3) 
    # "QApplication: invalid style override passed, ignoring it."
    sys.argv += ['-style', 'Fusion'] 
            
    app = QtWidgets.QApplication(sys.argv) #QApplication([]) #
    win = MyWindow()
    win.show()
    app.exec_()
