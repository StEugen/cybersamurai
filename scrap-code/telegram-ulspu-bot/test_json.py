import json, pprint, re
from urllib.request import Request, urlopen
from dates import dates



def get_json():
    f = open('test', 'w')
    with open('test2', 'r') as f2:
        text = [line.strip() for line in f2] 
    Lukianov = f'https://www.ulspu.ru/students/schedule/prepod/cb4ba39a83855bae2c56ff82453c7511-15.json'
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



id = f'https://www.ulspu.ru/students/schedule/prepod/cb4ba39a83855bae2c56ff82453c7511-'


def take_date():
    f = open('test2', 'w')
    for item in dates:
        item = item[:-3]
        text = id+f'{item}.json'
        f.write(text)
        f.write('\n')
        #return text
        

take_date()
get_json()