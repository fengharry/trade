# -*- coding:utf-8 -*- 

from pytdx.hq import TdxHq_API
     
if __name__ == "__main__":   
    api = TdxHq_API()
    c = api.connect('101.227.73.20', 7709)
    if not c:
        print('cannot connect to server')
        api.disconnect()
    dd = api.get_finance_info(0, '000001')
    print(dd['ipo_date']) 
