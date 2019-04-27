# -*- coding:utf-8 -*- 
#券商持股

import string
import tushare as ts

import sys
reload(sys)
sys.setdefaultencoding('utf8')

def func1(code):
    try:
        df = pro.top10_floatholders(ts_code=code, start_date='20180901', end_date='20190331')
    except:
        return 0
    #print(df.holder_name)
    ss="证券股份"
    for name in df.holder_name:
        aa=str(name)
        if (aa.find(str(ss))!=-1):
            #print(name.decode('UTF-8').encode('GBK'))
            return 1
    return 0
       
if __name__ == "__main__":   
    ts.set_token('fb2adceff6cb3b79b84ff677bbf16100f7b50db018769d8ab4245766')
    pro = ts.pro_api()
    data = pro.stock_basic(exchange='', list_status='L', fields='ts_code')
    #print(data)
    for code in data.ts_code:
        if(func1(code)>0):
            print(code)
