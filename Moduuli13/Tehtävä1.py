from flask import Flask, Response
import json

app = Flask(__name__)

def onko_alkuluku(luku):
    if luku <= 1:
        return False
    elif luku <= 3:
        return True
    elif luku % 2 == 0 or luku % 3 == 0:
        return False
    else:
        i = 5
        while i * i <= luku:
            if luku % i == 0 or luku % (i + 2) == 0:
                return False
            i += 6
        return True

@app.route('/alkuluku/<luku>')
def main(luku):
    if tilakoodi == 200:
        luku = int(luku)
        if onko_alkuluku(luku):
            vastaus = {
                "Numero": luku,
                "Alkuluku": True
            }
            
    json_data = json.dumps(vastaus)
    return Response(response=json_data, status=tilakoodi, mimetype='application/json')


if __name__ == "__main__":
    app.run(use_reloader=True, host='127.0.0.1', port=3000)


