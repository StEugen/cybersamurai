import json, pprint, re
from urllib.request import Request, urlopen

#text = f'https://www.ulspu.ru/students/schedule/prepod/cb4ba39a83855bae2c56ff82453c7511-15.json'

def get_json(text):
    f = open('test.txt', 'w')
    Lukianov = text
    req = Request(
        url=Lukianov,
        headers={'User-Agent': 'Mozila/5.0'})
    site = urlopen(req)
    data = json.load(site)
    for item in data:
        for i in data[item]:
            text = f'date: {item}\n location: {i["location"]}, group: {i["teachers"]}, time: {i["time"]}, subject: {i["subject"]}, type: {i["type"]}\n'
            text = re.sub('T13:00:00', '', text)
            f.write(text)
    
def take_info():
    f = open('test.txt', 'r')
    text = f.read()
    return text

#get_json(text)
#take_info()
