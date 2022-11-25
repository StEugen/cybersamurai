import requests
 
# Making a get request
response = requests.get('http://192.168.1.8/students/schedule/prepod/')
 
# print response
print(response)
 
# print json content
print(response.json())