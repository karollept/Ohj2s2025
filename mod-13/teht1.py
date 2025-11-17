#Toteuta Flask-taustapalvelu, joka ilmoittaa, onko parametrina saatu luku alkuluku vai ei.
# Hyödynnä toteutuksessa aiempaa tehtävää, jossa alkuluvun testaus tehtiin.
# Esimerkiksi lukua 31 vastaava GET-pyyntö annetaan muodossa: http://127.0.0.1:3000/alkuluku/31.
#Vastauksen on oltava muodossa: {"Number":31, "isPrime":true}.

from flask import Flask, Response
import json

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
    json_vastaus = json.dumps(vastaus)
    return Response(json_vastaus, content_type='application/json')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)