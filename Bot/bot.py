import requests
import ip

from curs import get_rate_today
from curs import get_rate_date

from time import sleep


token = ip.token


URL = 'https://api.telegram.org/bot' + token + '/'

global last_update_id
last_update_id = 0




def get_updates():
	url = URL + 'getupdates'
	r = requests.get(url)
	return r.json()

def get_last_message():

	data = get_updates()

	last_object = data['result'][-1]

	update_id = last_object['update_id']

	global last_update_id
	if last_update_id != update_id:
		last_update_id = update_id

		chat_id = last_object['message']['chat']['id']
		message_text = last_object['message']['text']

		message = {'chat_id': chat_id,
					'text': message_text}
		return message
	else:	
		return None			




def send_message(chat_id, text='Wait a second, please...'):
	url = URL + 'sendmessage?chat_id={}&text={}'.format(chat_id, text)
	
	requests.get(url)

def main():
	
	while True:
		answer = get_last_message()

		if answer != None:
			chat_id = answer['chat_id']
			text = answer['text']

			if text == '/rub':
				send_message(chat_id, get_rate_today())
			if text == '/usd_2016-07-05':
				send_message(chat_id, get_rate_date())	
		else:
			continue

		sleep(6) 			


if __name__ == '__main__':
	main()
