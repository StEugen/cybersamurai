import json, pprint, re
from urllib.request import Request, urlopen

def teacher_json():
    """ should read users input and produce id of teacher """
    f = open('files/teachers', 'w')
    week = input("Week: ")
    sname = input("Sname: ")
    req = Request(
        url=f'https://www.ulspu.ru/students/schedule/prepod/groups-{week}.json',
        headers={'User-Agent': 'Mozila/5.0'}
    )
    site = urlopen(req)
    data = json.load(site)
    #text = f'{data}'
    #f.write(text)
    #f.write('\n')
    for item in data['data']:
        if sname == item['text']:
            #print("Hell ya")
            #text = item['text']
            id = item['id']
            #f.write(text)
            #f.write('\n')
            f.write(id)
            break


teacher_json()

def get_json(text):
    """ takes url for json and generates readable text """
    f = open('files/test', 'w')
    id = f'https://www.ulspu.ru/students/schedule/prepod/cb4ba39a83855bae2c56ff82453c7511-'
    req = Request(
        url=id+f'{text}.json',
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
    f = open('files/test', 'r')
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

