# -*- coding:utf-8 -*- 

import tushare as ts
from pytdx.hq import TdxHq_API

api = TdxHq_API()

def func1(year, month):
    df = ts.xsg_data(year, month)
    df1 = df[df['ratio'].astype('float')>5]
    df2 = df1['code']
    date = 0
    for code in df2:
        if(code < '600000'):
            date = func2(0, code)
        else:
            date = func2(1, code)
        if(date < 20140000):
            print(code)
    return
      
def func2(market, code):
    info = api.get_finance_info(market, code)
    if (info != None):
        return info['ipo_date']
    else:
        return 20180000

if __name__ == "__main__":   
    
    c = api.connect('101.227.73.20', 7709)
    if not c:
        print('cannot connect to server')
        api.disconnect()
    
    func1('2017', '1')  
