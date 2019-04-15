import requests

form = {'name': 'James', 'last_name': 'Bond'}
r = requests.post('http://localhost:8080', data=form)
print(r.text)
