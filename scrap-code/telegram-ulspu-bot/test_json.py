import json, pprint
from urllib.request import Request, urlopen



def get_json():
    Lukianov = f'https://www.ulspu.ru/students/schedule/prepod/cb4ba39a83855bae2c56ff82453c7511-15.json'
    req = Request(
        url=Lukianov,
        headers={'User-Agent': 'Mozila/5.0'})
    site = urlopen(req)
    json_dump = json.dumps(site)
    dic = json.loads(json_dump)
    print(dic[0])
    data = json.load(site)
    #pprint.pprint(data)
    #return data

    for item in data:
        #text = f'date: {item["location"]}'
        text = data
        print(text)


get_json()
