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
        
    def get_rate_today(self, price):

        url='http://www.nbrb.by/API/ExRates/Rates/145'
        response=requests.get(url).json()
        price=response['Cur_OfficialRate']
        self. price=price 
        self. price==self. get_last_message()
        if self. price==’usd’:
            self. send_message(self. price)
        return str(self. price)+' today'
        
    def get_rate_date(self):
        url='http://www.nbrb.by/API/ExRates/Rates/145?onDate=2016-5-7'
        response=requests.get(url).json()
        data=response['Date']
        return str(data)
    
    def usd(self):
        lol=self.get_chat_id()
        chat_id=lol['chat_id']
        if curs=='usd':
            self.send_message(chat_id,self.get_rate_today())
        if curs=='Data':
                self.send_message(chat_id,self.get_rate_date())
  
        
    

      
        
                         
print(Mybot(var.bot_token).usd())
