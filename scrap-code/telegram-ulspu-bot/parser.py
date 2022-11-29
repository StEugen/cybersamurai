import requests, urllib, json

data = requests.get('https://www.ulspu.ru/students/schedule/prepod/cb4ba39a83855bae2c56ff82453c7511-17.json?0.42403647695275737')
print(data.json)
