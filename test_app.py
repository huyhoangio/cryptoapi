import requests

LOCAL_TEST_CONTAINER = 'http://127.0.0.1:5000'

def test_should_fail_if_api_not_respond():
	r = requests.get("{}/health".format(LOCAL_TEST_CONTAINER))

	assert r.status_code == 200


def test_should_fail_if_currency_not_supported_by_our_api():
	r = requests.get("{}/VND".format(LOCAL_TEST_CONTAINER))

	assert r.status_code == 404


def test_should_fail_if_currency_not_supported_by_coinbase_api():
	r = requests.get("{}/XYZ".format(LOCAL_TEST_CONTAINER))

	assert r.status_code == 404


def test_should_fail_if_can_not_parse_coinbase_data():
	r = requests.get("{}/JPY".format(LOCAL_TEST_CONTAINER))

	assert 'data' in r.json() or 'error' in r.json()
	

def test_should_pass_if_legit_currency_passed_in():
	r = requests.get("{}/USD".format(LOCAL_TEST_CONTAINER))

	assert r.status_code == 200
	assert 'data' in r.json()