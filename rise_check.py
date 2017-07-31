# -*- coding:utf-8 -*- 

import tushare.stock.trading as td
from datetime import *
import time

import smtplib
from email.mime.text import MIMEText
from email.header import Header

FROM = 'fengharry02@126.com'
TO = 'fengharry02@126.com'
server = smtplib.SMTP('smtp.126.com')
TEST = 0;

class stock_info:
    def __init__(self, a):
        self.stock_code = a; # 股票代码
        self.price = 0; # 比较价格
        
        self.message = MIMEText('Hello', 'plain', 'utf-8')
        self.message['From'] = FROM
        self.message['To'] = TO
        return

    def check_code(self):
        df = td.get_realtime_quotes(self.stock_code)
        if(self.price == 0):
            self.price = float(df['pre_close'])
        rise1 = 100 * (float(df['price']) - self.price) / self.price
        if(abs(rise1) > 0.5):
            self.price = float(df['price'])
            rise2 = 100 * (float(df['price']) - float(df['pre_close'])) / float(df['pre_close'])
            SUBJECT = self.stock_code + ' %.2f'%(rise2)
            if((rise2 > 1) and (rise1 < 0)):
                SUBJECT = 'sell ' + SUBJECT
            elif((rise2 < -1) and (rise1 > 0)):
                SUBJECT = 'buy ' + SUBJECT
            print(SUBJECT)
            if(TEST == 0):
                self.message['Subject'] = Header(SUBJECT, 'utf-8')
                server.sendmail(FROM, TO, self.message.as_string())
        return
       
if __name__ == "__main__":  
    server.login(FROM, 'test02') 
    
    a1 = stock_info('002422')
    a2 = stock_info('000536')
      
    while 1:
        a1.check_code()
        a2.check_code()
        
        time.sleep(120)
        
    server.quit()