import requests
import json
from pprint import pprint
main_link = 'https://api.github.com'
user = 'Boris13373'
r = requests.get(f'{main_link}/users/{user}/repos')
with open('data.json', 'w') as f:
    json.dump(r.json(), f)
    for i in r.json():
        pprint(f"Список репозиториев {i['name']}")
