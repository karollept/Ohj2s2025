#Kirjoita ohjelma, joka hakee ja tulostaa satunnaisen Chuck Norris -vitsin käyttäjälle.
# Käytä seuravalla sivulla esiteltävää rajapintaa: https://api.chucknorris.io/.
# Käyttäjälle on näytettävä pelkkä vitsin teksti.

import requests
import json

#find random joke from https://api.chucknorris.io/

vitsi = "https://api.chucknorris.io/jokes/random"
vastaus = requests.get(vitsi).json()

#print random joke
json_vastaus = vastaus.json()
for a in json_vastaus:
    print(json_vastaus['value'])
    break