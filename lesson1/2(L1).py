
import requests
import json
from pprint import pprint
params = { 'v' : '5.130',
           'access_token' : '931c2b53545949fb2580a712a96a5ba5c2a63c4a2abd7546e3702b7dc969d241f16917667015894bd4a1d',
           'user_id':'79385503',
           'extended' : '1'
          }
api = '931c2b53545949fb2580a712a96a5ba5c2a63c4a2abd7546e3702b7dc969d241f16917667015894bd4a1d'
main_link = 'https://api.vk.com/method/groups.get'

r = requests.get(main_link, params=params)
response = r.json()
with open('gr.json', 'w') as f:
    json.dump(response, f)
    for i in response.get("response").get("items"):
        pprint(f'- {i.get("name")}')