#!/usr/bin/env python3

# https://doc.qt.io/qt-5/qtextdocumentwriter.html
# https://code.woboq.org/qt5/qtbase/src/gui/text/qtextdocument.cpp.html

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtPrintSupport import QPrinter
import sys
import zipfile
import lxml.etree

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
        self.on_read(None)

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

        with zipfile.ZipFile('output.odf') as zh:
            data = zh.read('content.xml')
            
        #self.editor.setText(data.decode('utf-8'))
        
        reader = QtCore.QXmlStreamReader(data)

        self.html = ''
        self.styles = dict()
        self.ident = 0

        while not reader.atEnd():
            reader.readNext()

            #print(' '*self.ident,  'name:', reader.name())
            #print(' '*self.ident,  'text:', reader.text())
            #print(' '*self.ident,  'tokenString:', reader.tokenString())
            #print(' '*self.ident,  'tokenType:', reader.tokenType())
            #if reader.isCharacters():
            #    print('readtext:', reader.readElementText())
            
            #~ if reader.isStartElement():
                #~ print(' '*self.ident,  '<{}>'.format(reader.name()))
                #~ print(' '*self.ident,  'text:', reader.text())
                #~ ident += 2
            #~ elif reader.isEndElement():
                #~ ident -= 2
                #~ #print(' '*self.ident,  'tokenString:', reader.tokenString())
                #~ #print(' '*self.ident,  'tokenType:', reader.tokenType())
                #~ print(' '*self.ident,  '</{}>'.format(reader.name()))
            #~ else:
                #~ #print(' '*self.ident,  'tokenString:', reader.tokenString())
                #~ #print(' '*self.ident,  'tokenType:', reader.tokenType())
                #~ print(' '*self.ident,  'text:', reader.text())
                #~ pass
                
            #print('attributes:', reader.attributes())
            #print('-----')
            name = reader.name()
            
            if name == '':
                #print('no name:', reader.tokenString(), reader.text(), end='')
                print(reader.text(), end='')
            elif name == 'automatic-styles':
                self.process_automatic_styles(reader)
            elif name == 'body':
                self.process_body(reader)
            else:
                print(reader.name(), reader.text(), end='')
                
        if reader.hasError():
            print('hasError:', reader.hasError())
            print('error:', reader.error()) 
            print('errorString:', reader.errorString()) 
            print('lineNumber:', reader.lineNumber()) 
            print('lineNumber:', reader.lineNumber()) 
        else:
            self.editor.setHtml(self.html)

    def process_style(self, reader):
        
        while not reader.atEnd():
            reader.readNext()

            name = reader.name()

    def process_body(self, reader):

        self.process_item(reader, 'body')

        self.html = ''
        
        while not reader.atEnd():
            reader.readNext()

            name = reader.name()

            if name == 'body':
                break
                

            if name == '':
                text = reader.text()
                self.html += text
                print(text, end='')
                
            elif name == 'line-break':
                self.process_item(reader, 'br')
                
            elif name == 'p':
                self.process_item(reader, 'p')
                    
            elif name == 'span':
                self.process_item(reader, 'span')
                    
            elif name == 'list':
                self.process_item(reader, 'ul')
                    
            elif name == 'list-item':
                self.process_item(reader, 'li')

        self.process_item(reader, 'body')

        if reader.hasError():
            print('hasError:', reader.hasError())
            print('error:', reader.error()) 
            print('errorString:', reader.errorString()) 
            print('lineNumber:', reader.lineNumber()) 
            print('lineNumber:', reader.lineNumber()) 

        
    def process_item(self, reader, tag):
        
        if reader.isStartElement():
            text = '<{}>'.format(tag)
            self.html += text
            print(text, end='')
            attributes = reader.attributes()
            attr = {attr.name():attr.value() for attr in attributes}
            if attr.get('style-name'):
                print('name:', attr.get('style-name'), self.styles.get(attr.get('style-name')))
        elif reader.isEndElement():
            text = '</{}>'.format(tag)
            self.html += text
            print(text, end='')
        else:
            print('{}: >{}<'.format(reader.name(), reader.text()))

        if reader.isCharacters():
            print('item isCharacters:', reader.readElementText())
        


    def process_automatic_styles(self, reader):

        self.process_item(reader, 'automatic-styles')

        current = None
        
        while not reader.atEnd():
            reader.readNext()

            name = reader.name()

            if name == 'automatic-styles':
                break

            if name == '':
                text = reader.text()
                self.html += text
                print(text, end='')
                
            elif name == 'style':
                self.process_style(reader)

                attributes = reader.attributes()
                attr = {attr.name():attr.value() for attr in attributes}
                
                current = attr.get('name')
                
                if current:
                    print('name:', current)
                    self.styles[current] = {'type': 'style'}
                    
                    if attr.get('family'):
                        self.styles[current]['family'] = attr.get('family')
                    
            elif name == 'list-style':
                self.process_style(reader)
                    
            elif name == 'text-properties':
                self.process_style(reader)

                attributes = reader.attributes()
                attr = {attr.name():attr.value() for attr in attributes}
                
                if current:
                    print('name:', current)
                    self.styles[current] = {'type': 'style'}
                    
                    if attr.get('family'):
                        self.styles[current]['family'] = attr.get('family')
                    
                    
            elif name == 'list-level-style-bullet':
                self.process_style(reader)
                    
            elif name == 'list-level-properties':
                self.process_style(reader)

            elif name == 'paragraph-properties':
                self.process_style(reader)

                attributes = reader.attributes()
                attr = {attr.name():attr.value() for attr in attributes}
                
                if current:
                    print('name:', current)
                    self.styles[current].update(attr)

        self.process_item(reader, 'automatic-styles')

        print(self.styles)
        
        if reader.hasError():
            print('hasError:', reader.hasError())
            print('error:', reader.error()) 
            print('errorString:', reader.errorString()) 
            print('lineNumber:', reader.lineNumber()) 
            print('lineNumber:', reader.lineNumber()) 

        
    def process_style(self, reader):
        
        if reader.isStartElement():
            attributes = reader.attributes()
            attr = {attr.name():attr.value() for attr in attributes}
            text = '<{} {}>'.format(reader.name(), attr)
            #print('attributes:', [attr.name() for attr in attributes])
            #print('attributes:', [attr.qualifiedName() for attr in attributes])
            #print('attributes:', [attr.namespaceUri() for attr in attributes])
            #print(attributes.value('style:name'))
            print(text, end='')
        elif reader.isEndElement():
            text = '</{}>'.format(reader.name())
            print(text, end='')
        else:
            print('{}: >{}<'.format(reader.name(), reader.text()), end='')

        
if __name__ == '__main__':
    # Linux Mint 18.3 problem with style (GTK2/GTK3) 
    # "QApplication: invalid style override passed, ignoring it."
    sys.argv += ['-style', 'Fusion'] 
            
    app = QtWidgets.QApplication(sys.argv) #QApplication([]) #
    win = MyWindow()
    win.show()
    app.exec_()
