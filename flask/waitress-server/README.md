
```
from flask import Flask

def create_app():
    app = Flask(__name__)
       
    @app.route('/')
    def index():
        return "Hello World!"

    return app
    
if __name__ == '__main__':
    app = create_app()
    app.run()
```

If code is in file `main.py` then you can run it as

    waitress-serve --call "main:create_app"

If you forget `:` then you can see `"Malformed application"` 

---

You can still run it as 

    python main.py 
    
----

[Waitress 1.3.0](https://docs.pylonsproject.org/projects/waitress/en/stable/runner.html)

---
    
https://stackoverflow.com/questions/25254022/flask-are-blueprints-necessary-for-app-factories 

https://flask.palletsprojects.com/en/1.1.x/patterns/appfactories/
