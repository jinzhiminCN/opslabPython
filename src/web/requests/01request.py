# encoding=UTF-8

import requests


req = requests.get('https://github.com')
print(type(req))
print(dir(req))
print(req.status_code)
print(req)
