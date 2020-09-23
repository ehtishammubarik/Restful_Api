import requests

url = 'http://127.0.0.1:8000/book-list/'
headers = {'Authorization': 'Token b89d32509444214e563a7868e2e8de69cafe825f'}
r = requests.get(url, headers=headers)
print(r.json())
