import requests

haku = input("Anna lentokentän icao koodi: ")
pyynto = f"http://127.0.0.1:5000/kenttä/{haku}"

vastaus = requests.get(pyynto)

if vastaus.status_code == 200:
    print(vastaus.json())
else:
    print("Virhe palvelupyynnössä:", vastaus.status_code)