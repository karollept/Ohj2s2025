#Toteuta taustapalvelu, joka palauttaa annettua lentokentän ICAO-koodia vastaavan lentokentän nimen ja
# kaupungin JSON-muodossa. Tiedot haetaan opintojaksolla käytetystä lentokenttätietokannasta.
# Esimerkiksi EFHK-koodia vastaava GET-pyyntö annetaan muodossa: http://127.0.0.1:3000/kenttä/EFHK.
# Vastauksen on oltava muodossa: {"ICAO":"EFHK", "Name":"Helsinki Vantaa Airport", "Municipality":"Helsinki"}.

import mysql.connector
from flask import Flask, Response
import json

yhteys = mysql.connector.connect(
    host="localhost",
    user="root",
    password="f3V3r_dr34m3r",
    autocommit=True,
    database="lk_approt",
    port=3306
)
cursor = yhteys.cursor()

app = Flask(__name__)

@app.route('/kenttä/<icao>')
def hae_kentta(icao):
    cursor.execute("SELECT name, municipality FROM airport WHERE ident = %s", (icao,))
    tulos = cursor.fetchone()
    if tulos:
        vastaus = {
            "ICAO": icao,
            "Name": tulos[0],
            "Municipality": tulos[1]
        }
    else:
        vastaus = {"error": "Kenttää ei löytynyt"}
    return Response(json.dumps(vastaus), content_type='application/json')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)