import requests
import json


# res = requests.get('https://solnechnyy.sinara-development.ru/#/houses/13632/presentation/small/ ')
res = requests.post('https://pb1382.profitbase.ru/api/v2/json/houses/13632',
                    data={"pb_api_key":"aed5ba22faea5061b5664ca46671aab7",
                          "pb_subdomain":"pb1382",
                          "referer":"https://solnechnyy.sinara-development.ru"})


##print(res.text)

with open('test.html', 'w+') as f:
    f.write(res.text.encode().decode())


responseJson = json.loads(res.text.encode().decode())

sectionsInHouse = responseJson['response']['sections']

for section in sectionsInHouse:
    floorsInSection = section['floors']

    for floor in floorsInSection:
        roomsInFloor = floor['properties']

        for room in roomsInFloor:
            print(room['number'], room['price'], room['area'])






