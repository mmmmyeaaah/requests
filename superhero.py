import requests

url = 'https://superheroapi.com/api/'
token = '2619421814940190'

def search_id(name):
    id = requests.get(f'{url}{token}/search/{name}')
    return id.json()['results'][0]['id']
   
def intelligence(name): 
    intel = requests.get(f'{url}{token}/{search_id(name)}')
    return int(intel.json()['powerstats']['intelligence'])

def superhero():
    if intelligence('Hulk') < intelligence('Thanos') > intelligence('Captain America'):
        print('Thanos умнее')
    elif intelligence('Thanos') < intelligence('Hulk') > intelligence('Captain America'):
        print('Hulk самый умный!')
    elif intelligence('Thanos') < intelligence('Captain America') > intelligence('Hulk'):
        print('Кэп умнее')
    else:
        print('Все умные!')       


if __name__ == '__main__':
    superhero()