import json, pprint, re
from urllib.request import Request, urlopen
from datetime import datetime





req = Request(
        url=f'https://www.ulspu.ru/students/schedule/prepod/465c5d910e8f014b2301dd93b30a53a9-15.json',
        headers={'User-Agent': 'Mozila/5.0'})
site = urlopen(req)
data = json.load(site)
sorted_date = sorted(data, key=lambda x: datetime.strftime(x['date'], '%m/%d/%Y'))
print(sorted_date)