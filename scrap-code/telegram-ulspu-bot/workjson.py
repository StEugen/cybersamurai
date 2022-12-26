import json, pprint, re
from urllib.request import Request, urlopen

def teacher_json(sname, week):
    """ should read users input and produce id of teacher """
    f = open('files/jsonhere', 'w')
    req = Request(
        url=f'https://www.ulspu.ru/students/schedule/prepod/groups-{week}.json',
        headers={'User-Agent': 'Mozila/5.0'}
    )
    site = urlopen(req)
    data = json.load(site)
    for item in data['data']:
        if sname == item['text']:
            id = item['id']
            f.write(id)
            break

def get_json():
    """ takes id, makes url for json and generates readable text """
    f = open('files/timetable', 'w')
    f2 = open('files/jsonhere', 'r')
    id = f2.read()
    req = Request(
        url=f'https://www.ulspu.ru/students/schedule/prepod/{id}.json',
        headers={'User-Agent': 'Mozila/5.0'})
    site = urlopen(req)
    data = json.load(site)
    for item in data:
        for i in data[item]:
            text = f'date: {item}\n location: {i["location"]},\n group: {i["teachers"]},\n time: {i["time"]},\n subject: {i["subject"]},\n type: {i["type"]}\n\n'
            text = re.sub('T13:00:00', '', text)
            f.write(text)

def take_info():
    """ trash function just to return text where timetable is"""
    f = open('files/timetable', 'r')
    text = f.read()
    return text
        
def get_dates():
    """ Write dates, so dates.py can work with them """
    f = open('files/dates', 'w')
    req = Request(
        url='https://www.ulspu.ru/students/schedule/prepod/weeks.json',
        headers={'User-Agent': 'Mozila/5.0'}
    )
    site = urlopen(req)
    data = json.load(site)
    for item in data:
        f.write(item)
        f.write('\n')

