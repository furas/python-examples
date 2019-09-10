from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World of Lambda+Flask+Zappa'
    
@app.route("/binary", methods=["POST"])
def create_binary():
    print(request.args)
    print(request.data)
    print(request.files)
    print(request.headers)
    
    if request.content_type == "application/octet-stream":
        data = request.get_data()
        print(len(data))
        print(data[:20])
        return jsonify({
            'msg': 'success',
            'request.content_type': request.content_type,
            'request.content_length': request.content_length,
            'len': len(data),
            'first': data[:20].decode('unicode_escape'), # convert bytes to string which can be send in JSON
        })
    else:
        return jsonify({
            'msg': '415 Unsupported Media Type ;)',
            'request.content_type': request.content_type,
        })

@app.route("/file", methods=["POST"])
def file():
    print(request.args)
    print(request.data)
    print(request.files)
    print(request.headers)
    
    file_ = request.files.get('file')

    if file_:
        #file_.save('output.pdf')
        data = file_.read()
        print(len(data))
        print(data[:20])
        return jsonify({
            'msg': 'success',
            'request.content_type': request.content_type,
            'request.content_length': request.content_length,
            'filename': file_.filename,
            'len': len(data),
            'first': data[:20].decode('unicode_escape'), # convert bytes to string which can be send in JSON
        })
    else:
        return jsonify({
            'msg': 'no file',
            'request.content_type': request.content_type,
        })
            
if __name__ == '__main__':
    app.run()    
