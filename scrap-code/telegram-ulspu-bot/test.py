import json, pprint
from urllib.request import Request, urlopen


req = Request(
    url='https://www.ulspu.ru/students/schedule/prepod/cb4ba39a83855bae2c56ff82453c7511-17.json',
    headers={'User-Agent': 'Mozila/5.0'})
site = urlopen(req)
data = json.load(site)
pprint.pprint(data)
