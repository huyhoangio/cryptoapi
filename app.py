from flask import Flask, jsonify, json, make_response
import requests
import os

app = Flask(__name__)

COINBASE_SPOT_ENDPOINT = os.environ['COINBASE_SPOT_ENDPOINT']

@app.route('/<string:currency>', methods=['GET'])
def get_currency_exchange(currency):
	acceptable_currency = ['EUR', 'GBP', 'USD', 'JPY']
	if currency not in acceptable_currency:
		return make_response(jsonify({ 'error': 'currency not supported'}), 404)
	
	r = requests.get('{0}{1}'.format(COINBASE_SPOT_ENDPOINT, currency))		
	if r.status_code == 404:
		return make_response(jsonify({ 'error': 'currency not available on coinbase'}), 404)
	elif r.status_code == 200:
		returned_data = r.json()
		if 'data' not in returned_data:
			return make_response(jsonify({ 'error': 'json can not be parsed or format has changed'}), 404)
		else:
			return make_response(jsonify({ 'data': returned_data['data']}), 200)

@app.route('/health', methods=['GET'])
def get_health():
	return make_response('It is running', 200)

if __name__ == '__main__':
	app.run(debug=True)