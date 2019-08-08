from bottle import route, run, request, redirect
from threading import Thread
import os


class File(Thread):
    def __init__(self, files):
        Thread.__init__(self)
        self.files = files

    def run(self):
        print('[thread] files:', self.files)
        for file in self.files:
            file.save("./save_file", overwrite=True)
            print("./save_file/" + file.filename)
            
            
@route('/') 
def index():
    """ 
    <form> with 'enctype="multipart/form-data"' gives files in request.files
    <form> with 'enctype="multipart/form-data"' gives files in request.query
    
    """
    
    print('[bottle] url: /')
    return '''
<form method="POST" action="/upload" enctype="multipart/form-data">
<input type="text" name="string"><br/>
<input type="file" name="file"/><br/>
<button type="submit">SEND</button>
</form>
'''

@route('/upload', method='POST') 
def file():
    print('[bottle] url: /upload')
    

    print('[bottle] query:', request.query.keys())
    print('[bottle] forms:', request.forms.keys())
    print('[bottle] files:', request.files.keys())
    
    files = request.files.getall('file')
    print('[bottle] files:', files)
    
    save_path = "./save_file"
    if not os.path.exists(save_path):
        os.mkdir(save_path)
    
    File(files).start()

    print('[bottle] redirect: /')
    redirect('/')
    # print('after redirect') # never executed

if __name__ == '__main__':
    run()
