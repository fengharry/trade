# -*- coding:utf-8 -*- 

import tushare as ts

import pandas as pd

def func1(year, month):
    df = ts.xsg_data(year, month)
    df1 = df[df['ratio'].astype('float')>5]
    print(df1)
    return
       
if __name__ == "__main__":   
    pd.set_option('display.height',2000) 
    
    func1('2017', '8')  
