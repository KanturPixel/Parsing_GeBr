import requests
import json


user = str(input('Enter username: '))
url = f"https://api.github.com"
r = requests.get(f'{url}/users/{user}/repos')
with open('data.json', 'w') as f:
    json.dump(r.json(), f)

for i in r.json():
    print(i['name'])
