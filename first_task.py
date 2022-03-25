import requests

URL = 'https://www.superheroapi.com/api.php/2619421814940190/search/'
superheroes = [{'name': 'Hulk'}, {'name': 'Captain America'}, {'name': 'Thanos'}]

intelligence = 0
name = ' '
for heroes in superheroes:
    response = requests.get(URL + heroes['name'])
    heroes_intelligence = int(response.json()['results'][0]['powerstats']['intelligence'])
    if intelligence < heroes_intelligence:
        intelligence = heroes_intelligence
        name = heroes['name']


print(f" {name}, is the most intelligent guy, his intelligence level is {intelligence}")









