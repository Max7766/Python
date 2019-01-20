import requests

def get_rate_today():
    url='http://www.nbrb.by/API/ExRates/Rates/145'
    response=requests.get(url).json()
    price=response['Cur_OfficialRate']
    return str(price)+' usd на сегодня'



def get_rate_date():
    url = 'http://www.nbrb.by/API/ExRates/Rates/145?onDate=2016-5-7'
    response=requests.get(url).json()
    price=response['Cur_OfficialRate']
    return str(price)+' курс USD на 2016-05-07 '

