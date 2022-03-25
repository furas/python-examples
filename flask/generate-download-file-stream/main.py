# author: Bartlomiej "furas" Burek (https://blog.furas.pl)
# date: 2022.03.12
# 

# it sends only some files from file 

# https://flask.palletsprojects.com/en/2.0.x/patterns/streaming/
# https://flask.palletsprojects.com/en/2.0.x/api/#flask.Response
# https://flask.palletsprojects.com/en/2.0.x/api/#flask.Flask.response_class

from flask import Flask, send_file
import io

data = '''smile id
0 CC(C)C(=O)Nc1nc2c(ncn2CC(=O)N2[C@@H]3CC[C@H]2C[C@@H](NC(=O)c2cnc[nH]2)C3)c(O)n1 ZINC001801458702
1 O=C(c1ccc(O)c([N+](=O)[O-])c1)N1CC[C@@]2(C1)CN(C(=O)[C@@H]1CC(=O)N(C3CCCC3)C1)CCO2 ZINC001781539777
2 C[C@@H]1CCc2c(C(=O)Nc3cc([C@@H]4CCCCN4C(=O)c4ccc5c(n4)NC(=O)CC5)[nH]n3)n[nH]c21 ZINC001818636963
3 O=C(CN1C(=O)C=CC1=O)N1CCC2(CCCN(C(=O)[C@H]3CCc4nc(O)nc(O)c4C3)C2)CC1 ZINC001807092425
4 NC(=O)c1nccnc1C(=O)N1CCC2(CCCN(C(=O)[C@@H]3CCc4nc(O)nc(O)c4C3)C2)CC1 ZINC001807092030'''

app = Flask(__name__)

def generate(start, end):
    f = io.StringIO(data)
    #f = open(filename, 'r')
    
    # skip lines
    for _ in range(start):
        f.readline()
        
    # send lines
    for i in range(end-start):
        yield f.readline()

@app.route('/')
@app.route('/<int:end>')
@app.route('/<int:start>/<int:end>')
def index(start=0, end=1):
    headers = {'Content-Disposition': 'attachment; filename="smile2.csv"'}
    response = app.response_class(generate(start, end), headers=headers, mimetype='text/csv')
    
    #response = app.response_class(generate(start, end), mimetype='text/csv')
    #response.headers['Content-Disposition'] = 'attachment; filename="smile.csv"'
    
    return response

if __name__ == '__main__':
    #app.debug = True 
    app.run()  
