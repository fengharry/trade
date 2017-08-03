# -*- coding:utf-8 -*- 

import tushare.stock.trading as td
from datetime import *
import time

import smtplib
from email.mime.text import MIMEText
from email.header import Header

ADDR = 'smtp.qq.com'
FROM = 'fengharry02@qq.com'
TO = 'fengharry02@126.com'

TEST = 0;

class stock_info:
    def __init__(self, a):
        self.stock_code = a; # 股票代码
        self.price = 0; # 比较价格
        return

    def check_code(self):
        df = td.get_realtime_quotes(self.stock_code)
        if((float(df['price']) == 0) or (float(df['pre_close']) == 0)): # 没开盘
            return
        if(self.price == 0):
            self.price = float(df['price'])
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
                message = MIMEText('Hello', 'plain', 'utf-8')
                message['From'] = FROM
                message['To'] = TO
                message['Subject'] = SUBJECT
                server = smtplib.SMTP_SSL(ADDR)
                server.ehlo(ADDR)
                server.login(FROM, 'cltduxqlmbmndjhg') 
                server.sendmail(FROM, TO, message.as_string())
                server.quit()
        return
       
if __name__ == "__main__":  
    a1 = stock_info('002422')
    a2 = stock_info('000536')
      
    while 1:
        a1.check_code()
        a2.check_code()
        
        time.sleep(120)