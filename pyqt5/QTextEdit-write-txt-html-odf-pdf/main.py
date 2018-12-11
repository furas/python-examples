#!/usr/bin/env python3

# https://doc.qt.io/qt-5/qtextdocumentwriter.html
# https://code.woboq.org/qt5/qtbase/src/gui/text/qtextdocument.cpp.html

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtPrintSupport import QPrinter
import sys
import zipfile

class OdfReader():
    
    def __init__(self, textedit, filename=None):
        self.textedit = textedit
        self.filename = filename
        
    def read(self, filename=None)
        if filename is not None:
            self.filename = filename
            
        if filename is None:
            raise Exception('you need filename')
            
class MyWindow(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()

        self.editor = QtWidgets.QTextEdit(self)
        self.editor.insertHtml('<b>bold text</b><br><i>italic text</i><br><ul><li>One<\li><li>One<\li></ul>')

        button_read = QtWidgets.QPushButton(self, text='READ')
        button_read.clicked.connect(self.on_read)
        
        button_write = QtWidgets.QPushButton(self, text='WRITE')
        button_write.clicked.connect(self.on_write)
        
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.editor)
        layout.addWidget(button_read)
        layout.addWidget(button_write)

        self.setLayout(layout)


    def on_write(self, event):
        #print(self.editor.toPlainText())
        #print(self.editor.toHtml())

        # https://doc.qt.io/qt-5/qtextdocumentwriter.html
        #writer = QtGui.QTextDocumentWriter('output.odf', b'ODF')
        #writer.write( self.editor.document() )

        writer = QtGui.QTextDocumentWriter()

        #for item in writer.supportedDocumentFormats():
        #    print('format:', bytes(item).decode())

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
        

    def on_read(self, event):
        with open('output.html') as fh:
            #self.editor.setHtml(fh.read())
            self.editor.setText(fh.read())
    
        self.read_odf('output.odf')
        
        
    def read_odf(self, filename):
        
        with zipfile.ZipFile(filename) as zh:
            data = zh.read('content.xml')
            
        print(data.decode('utf-8'))
        #self.editor.setText(data.decode('utf-8'))
        
        reader = QtCore.QXmlStreamReader(data)

        while not reader.atEnd():
            reader.readNext()

            #print('next:', reader.readNext())
            print('tokenString:', reader.tokenString())
            print('tokenType:', reader.tokenType())
            print('name:', reader.name())
            print('prefix:', reader.prefix())
            print('qualifiedName:', reader.qualifiedName())
            print('text:', reader.text())
            print('namespaceDeclarations:', reader.namespaceDeclarations())
            print('namespaceUri:', reader.namespaceUri())
            #if reader.isCharacters():
            #    print('readtext:', reader.readElementText())
            #print('isStartElement', reader.isStartElement())
            #print('attributes:', reader.attributes())
            for item in reader.attributes():
                print('attribut>', item.name(), item.value())
            print('-----')
            
        if reader.hasError():
            print('hasError:', reader.hasError())
            print('error:', reader.error()) 
            print('errorString:', reader.errorString()) 
            print('lineNumber:', reader.lineNumber()) 
            print('columnNumber:', reader.columnNumber()) 
            print('characterOffset:', reader.characterOffset()) 


if __name__ == '__main__':
    # Linux Mint 18.3 problem with style (GTK2/GTK3) 
    # "QApplication: invalid style override passed, ignoring it."
    sys.argv += ['-style', 'Fusion'] 
            
    app = QtWidgets.QApplication(sys.argv) #QApplication([]) #
    win = MyWindow()
    win.show()
    app.exec_()
