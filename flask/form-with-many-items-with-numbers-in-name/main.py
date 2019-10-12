from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':

        print('--- original order ---')
        
        for key, val in request.form.items():
            if key.startswith("item"):
                print(key, val)

        print('--- sorted ---')
        
        keys = [key for key in request.form.keys() if key.startswith("item")]
        keys = sorted(keys)
        
        for key in keys:
            #print(key, request.form[key])
            print(key, request.form.get(key))
            
    return render_template_string('''Items in random order</br>
<form method="POST">
<input name="item4" value="val4"/></br>
<input name="item2" value="val2"/></br>
<input name="item1" value="val1"/></br>
<input name="item3" value="val3"/></br>
<button type="submit">OK</button>
</form>
''')

app.run(debug=False)
