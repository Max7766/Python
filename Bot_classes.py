import requests
import info as var



class Mybot:
    upd=var.methods['updates']
    send=var.methods['send']
    tel_api_url=var.telegram_ipi_url
    def __init__(self,bot_token='733692742:AAGFVkN8NV3kxNA_1HVpvOHOKyKMXu7Ifuo/'):
        self.token=bot_token

        
    def get_updates(self):
        res=requests.get(self.tel_api_url.format(self.token)+self.upd)
        return res.json()
        
    def get_chat_id(self):
        chat_id=self.get_updates()['result'][-1]['message']['chat']['id']
        return chat_id
    
    def get_last_message(self):
        last_mess=self.get_updates()['result'][-1]['message']['text']
        return last_mess
    
    def send_message(self):
        chat_id=self.get_chat_id()
        text=self.get_last_message()
        params={'chat_id':chat_id,'text':text}
        requests.post(self.tel_api_url.format(self.token)+self.send,params)
        
    def get_rate_today(self):
        url='http://www.nbrb.by/API/ExRates/Rates/145'
        resp=requests.get(url).json()
        price=resp['Cur_OfficialRate']
        return str(price)
        
    def get_rate_date(self):
        url='http://www.nbrb.by/API/ExRates/Rates/145?onDate=2016-5-7'
        response=requests.get(url).json()
        data=response['Date']
        return str(data)
    
    def usd(self):
        curs=self.get_last_message()
        if curs=='usd':
            self.send_message(curs,self.get_rate_today())
        if curs=='Data':
                self.send_message(curs,self.get_rate_date())
                
    def type(self):
        text=self.get_last_message()
        if type(text)!=str:
            self.send_message(text,'вы ввели текст неверного типа,введите валюту')
        else:
            return 'Youre type is -str-',text
            
   
    def status(self):
        res=self.tel_api_url.format(self.token)+self.upd
        status=requests.get(res)
        if status.status_code==200:
            return 'Соединение хорошее',status.status_code
        if status.status_code==404 or 303:
            return 'Соединение плохое',status.status_code

        
    def posledni_text(self):
        message=self.get_last_message()
        three=self.get_updates()['result'][-3]['message']['text']
        if message=='Что я писал 3 сообщения назад':
            return '3 сообщения назад ты писал',three
        
    

      
        
                         
print(Mybot(var.bot_token).status())
   

        
            
        
    
    

