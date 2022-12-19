import json, pprint, re
from urllib.request import Request, urlopen



def get_json():
    Lukianov = f'https://www.ulspu.ru/students/schedule/prepod/cb4ba39a83855bae2c56ff82453c7511-15.json'
    req = Request(
        url=Lukianov,
        headers={'User-Agent': 'Mozila/5.0'})
    site = urlopen(req)
    data = json.load(site)
    dictionary = []
    for item in data:
        for i in data[item]:
            text = f'date: {item},\n location: {i["location"]}, group: {i["teachers"]}, time: {i["time"]}, subject: {i["subject"]}, type: {i["type"]}'
            text = re.sub('T13:00:00', '', text)
            return text

#get_json()