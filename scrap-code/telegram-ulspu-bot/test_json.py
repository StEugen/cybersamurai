import json, pprint
from urllib.request import Request, urlopen

week = input("Enter week number: ")
day = input("Enter the day: ")
year = input("Enter the year: ")
month = input("Enter the month: ")
today_data = f'{year}-{month}-{day}T13:00:00'
Lukianov = f'https://www.ulspu.ru/students/schedule/prepod/cb4ba39a83855bae2c56ff82453c7511-{week}.json'
req = Request(
    url=Lukianov,
    headers={'User-Agent': 'Mozila/5.0'})
site = urlopen(req)
data = json.load(site)
#pprint.pprint(data)
pprint.pprint(data[today_data])
