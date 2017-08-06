# -*- coding:utf-8 -*- 

import tushare as ts

def func1(year, month):
    df = ts.xsg_data(year, month)
    df1 = df[df['ratio'].astype('float')>5]
    print(df1.ratio.count())
    return
       
if __name__ == "__main__":   
    print('2017 限售解禁:')
    for i in range(1,13):
        func1('2017', i) 
    
    print('2018 限售解禁:')
    for i in range(1,13):
        func1('2018', i)    
