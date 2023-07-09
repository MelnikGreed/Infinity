import requests
import json

url = 'https://akabab.github.io/superhero-api/api/all.json'
response = requests.get(url)
heroes = response.json()
heroes_name = []
heroes_name.append(heroes[106])
heroes_name.append(heroes[236])
heroes_name.append(heroes[506])
dict_heroes = {}
for heroes in heroes_name:
    dict_heroes[heroes['name']] = heroes['powerstats']['intelligence']
heroes_sort = {k: v for k, v in sorted(dict_heroes.items(), key=lambda item: item[1], reverse=True)}
print(f'Самый умный супергерой {list(heroes_sort.keys())[0]} ~ "я сама неотвратимость"')
