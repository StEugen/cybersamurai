import json, pprint, re
from urllib.request import Request, urlopen
from dates import dates


id = f'https://www.ulspu.ru/students/schedule/prepod/cb4ba39a83855bae2c56ff82453c7511-'

## создает json ссылки на основе дат
#def take_date(text):
#    f = open('files/jsonhere', 'w')
#    for item in dates:
#        item = item[:-3]
#        text = id+f'{item}.json'
#        f.write(text)
#        f.write('\n')
#text = '15-16'
## берет необходимую json ссылку и генирирует на основе ее читабельный формат
def get_json(text):
    f = open('files/test', 'w')
    #with open('files/jsonhere', 'r') as f2:
    #    text = [line.strip() for line in f2] 
    id = f'https://www.ulspu.ru/students/schedule/prepod/cb4ba39a83855bae2c56ff82453c7511-'
    item = text[:-3]
    to_msg = id+f'{item}.json'
    req = Request(
        url=to_msg,
        headers={'User-Agent': 'Mozila/5.0'})
    site = urlopen(req)
    data = json.load(site)
    for item in data:
        for i in data[item]:
            text = f'date: {item}\n location: {i["location"]},\n group: {i["teachers"]},\n time: {i["time"]},\n subject: {i["subject"]},\n type: {i["type"]}\n\n'
            text = re.sub('T13:00:00', '', text)
            f.write(text)

## мусорная функция, возвращает переменную text, в которой хранится расписание
def take_info():
    f = open('files/test', 'r')
    text = f.read()
    return text

#get_json(text)

        
#take_date()
        
