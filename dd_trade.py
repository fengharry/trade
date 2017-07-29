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
    def __init__(self, a, b):
        self.stock_code = a; # 股票代码
        self.stock_num = b; # 大单手数
        self.count = 0; # 大单笔数
        self.rise = 0.0; # 涨跌幅
        
        self.message = MIMEText('Hello', 'plain', 'utf-8')
        self.message['From'] = FROM
        self.message['To'] = TO
        return

    def check_code(self):
        df = td.get_realtime_quotes(self.stock_code)
        self.rise = 100 * (float(df['price']) - float(df['pre_close'])) / float(df['pre_close'])
        print(self.rise)
        
        df = td.get_sina_dd(self.stock_code, date.today(), self.stock_num)
        if (df is None):
            return
        elif (df['type'].count() == self.count) or (df['type'].count() < 2):
            print('no new data')
            return
        else:
            self.count = df['type'].count()
    
        print(df)
        if (df['type'][0] == '卖盘') and (df['type'][1] == '卖盘') and (df['price'][0] <= df['price'][1]):
            SUBJECT = 'sell ' + self.stock_code + ' @' + str(df['price'][0])
            print(SUBJECT)
            if(TEST == 0):
                self.message['Subject'] = Header(SUBJECT, 'utf-8')
                server.sendmail(FROM, TO, self.message.as_string())
        elif (df['type'][0] == '买盘') and (df['type'][1] == '买盘') and (df['price'][0] >= df['price'][1]):
            SUBJECT = 'buy ' + self.stock_code + ' @' + str(df['price'][0])
            print(SUBJECT)
            if(TEST == 0):
                self.message['Subject'] = Header(SUBJECT, 'utf-8')
                server.sendmail(FROM, TO, self.message.as_string())
        return
       
if __name__ == "__main__":  
    server.login('fengharry02@126.com', 'test02') 
    
    a1 = stock_info('002422', 200)
    a2 = stock_info('000536', 600)
      
    while 1:
        a1.check_code()
        a2.check_code()
        
        time.sleep(300)
        
    server.quit()