#Tutustu avoimeen OpenWeather-säärajapintaan: https://openweathermap.org/api.
# Kirjoita ohjelma, joka kysyy käyttäjältä paikkakunnan nimen ja tulostaa sitä vastaavan säätilan
# tekstin sekä lämpötilan Celsius-asteina. Perehdy rajapinnan dokumentaatioon riittävästi.
# Palveluun rekisteröityminen on tarpeen, jotta saat rajapintapyynnöissä tarvittavan API-avaimen (API key).
# Selvitä myös, miten saat Kelvin-asteet muunnettua Celsius-asteiksi.
import json
import requests

#ask city
haku = input("anna kaupunki jonka sään haluat tietää: ")

pyynto = f"https://api.openweathermap.org/data/2.5/weather?q={haku}&APPID=573f80037fa66190f60878e34617be86"
vastaus = requests.get(pyynto)

#print city weather text and temperature in celcius
# kelvin to celcius
# 273,15K = 0Celsius

json_vastaus = vastaus.json()
for a in json_vastaus['weather']:
    saatila = a['main']
    lampotila = json_vastaus['main']['temp']
    c_lampotila = lampotila - 273.15
    print(f"In the city of {haku} the current weather is {saatila},")
    print(f"and the temperature is {c_lampotila:.1f} °C.")
    break