from flask import Flask, jsonify
import webbrowser
from mongo import Mongo

app = Flask(__name__)
db_client = Mongo().client
db = db_client.get_database('EXAMENFINAL')
col = db.get_collection('autos')

@app.route('/')
def index():
    autos = list(col.find({}))
    response = []
    for auto in autos:
        response.append({
            'marca': auto['marca'],
            'precio': auto['precio'],
            'caracteristicas': auto['caracteristicas']
        })
    return jsonify(response)

if __name__ == '__main__':
    webbrowser.open('http://127.0.0.1:5000')
    app.run(debug=True)
