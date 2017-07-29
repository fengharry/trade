# -*- coding:utf-8 -*- 

import tushare as ts

def func1(year, month):
    df = ts.xsg_data(year, month)
    df1 = df[df['ratio'].astype('float')>5]
    print(df1.ratio.count())
    return
       
if __name__ == "__main__":   
    print('2017 限售解禁:')
    func1('2017', '1')    
    func1('2017', '2')    
    func1('2017', '3')    
    func1('2017', '4')    
    func1('2017', '5')    
    func1('2017', '6')    
    func1('2017', '7')    
    func1('2017', '8')    
    func1('2017', '9')    
    func1('2017', '10')    
    func1('2017', '11')    
    func1('2017', '12') 
    
    print('2018 限售解禁:')
    func1('2018', '1')    
    func1('2018', '2')    
    func1('2018', '3')    
    func1('2018', '4')    
    func1('2018', '5')    
    func1('2018', '6')    
    func1('2018', '7')    
    func1('2018', '8')    
    func1('2018', '9')    
    func1('2018', '10')    
    func1('2018', '11')    
    func1('2018', '12')    
