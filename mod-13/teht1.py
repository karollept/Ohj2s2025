#Toteuta Flask-taustapalvelu, joka ilmoittaa, onko parametrina saatu luku alkuluku vai ei.
# Hyödynnä toteutuksessa aiempaa tehtävää, jossa alkuluvun testaus tehtiin.
# Esimerkiksi lukua 31 vastaava GET-pyyntö annetaan muodossa: http://127.0.0.1:3000/alkuluku/31.
#Vastauksen on oltava muodossa: {"Number":31, "isPrime":true}.

from flask import Flask, request

app = Flask(__name__)

def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

@app.route('/alkuluku/<int:luku>')
def tarkista_alkuluku(luku):
    vastaus = {
        "Number": luku,
        "isPrime": isPrime(luku)
    }
    return (vastaus)

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)

haku = input("Anna numero josta haluat tietää onko se alkuluku: ")
pyynto = f"http://127.0.0.1:3000/alkuluku/{haku}"

vastaus = requests.get(pyynto)
print(vastaus.json())