import requests


def get_rate_today():
	
	url = 'http://www.nbrb.by/API/ExRates/Rates/298'
	
	response = requests.get(url).json()
	return str(response)

def get_rate_date():
	
	url = 'http://www.nbrb.by/API/ExRates/Rates/298?onDate=2016-7-5'

	response = requests.get(url).json()
	return str(response)
