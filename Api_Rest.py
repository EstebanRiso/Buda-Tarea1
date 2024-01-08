from flask import Flask,jsonify
import json
from Spread import SpreadMercados, SpreadMercado, SpreadCompare, SpreadCompareAll


app = Flask(__name__)

@app.route('/api/v2/spreads/all/', methods=['GET'])
def mercados():

    json_string = SpreadMercados()
    python_dict = json.loads(json_string)
    return jsonify(python_dict)

@app.route('/api/v2/spreads/<market_id>', methods=['GET'])
def mercado(market_id):

    json_string = SpreadMercado(market_id,singular=True)
    python_dict = json.loads(json_string)

    return jsonify(python_dict)


@app.route('/api/v2/polling/spread/<market_id>/<float:spread>', methods=['GET']) #consulta en un mercado specifico, un spread
def spread_query(market_id,spread):
    if isinstance(spread,float):
        json_string=SpreadCompare(spread,market_id,singular=True)
        python_dict=json.loads(json_string)
    else:
        json_string='{status: "Error: no es una variable flotante"'
        json_string=json_string+'}'


    return jsonify(python_dict)



@app.route('/api/v2/polling/spread/all/<float:spread>', methods=['GET'])
def spread_query_all(spread):

    if isinstance(spread,float):
        json_string=SpreadCompareAll(spread)
        python_dict=json.loads(json_string)
    else:
        print("no es flotante, se requiere que el parametro sea flotante")
        
        json_string='{"status": "Error, no es una variable flotante"'
        json_string=json_string+'}'
        python_dict=json.loads(json_string)


    return jsonify(python_dict)




if __name__ == '__main__':
    app.run(debug=True)