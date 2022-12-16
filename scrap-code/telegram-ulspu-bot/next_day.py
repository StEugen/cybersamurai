import json, pprint
from urllib.request import Request, urlopen
import os
import datetime

print("Weeks: 15, 17, 19, 21, 23, 25")
week = input()
whatDay = input("Week, today or tomorrow: ")
withTime = datetime.datetime.now()
nextwithoutTime = withTime.date() + datetime.timedelta(days=1)
todayWithoutTime = withTime.date()
nextday_data = f'{nextwithoutTime}T13:00:00'
today_data = f'{todayWithoutTime}T13:00:00'
#print(nextday_data)
Lukianov = f'https://www.ulspu.ru/students/schedule/prepod/cb4ba39a83855bae2c56ff82453c7511-{week}.json'
req = Request(
    url=Lukianov,
    headers={'User-Agent': 'Mozila/5.0'})
site = urlopen(req)
data = json.load(site)
if whatDay == "week" or whatDay=="Week":
    pprint.pprint(data)
elif whatDay=="today" or whatDay=="Today":
    pprint.pprint(data[today_data])
elif whatDay=="tommorrow" or whatDay=="Tomorrow":
    pprint.pprint(data[nextday_data])
else:
    "Null"