import requests
import json

response = requests.get('https://api.stackexchange.com/2.3/questions?order=desc&sort=activity&site=stackoverflow')
'''keysList = list(response.json()['items'][0].keys())
print(keysList)

print(response.json()['items'][0])'''

'''for question in response.json()['items']:
    print(question['title'])'''

for question in response.json()['items']:
    if question['answer_count']<2:
        print(question['title'])
        print(question['link'])
        print()