# -*- coding:utf-8 -*- 

import traceback

def func1():
    a = 1/0
    print('func1')
    return

def func2():
    try:
        a = 1/0
    except:
        traceback.print_exc()
    print('func2')
    return

def func3():
    file_data = open('data/log.txt')
    for i in range(1,22):
        file_name = 'data/data%d.txt'%(i)
        file_tmp = open(file_name, 'w')
        try:
            for j in range(1,26):
                one_line = file_data.readline()
                file_tmp.write(one_line)
        except:
            traceback.print_exc()
        file_tmp.close()
    file_data.close()
    return
       
if __name__ == "__main__":  
    func3()
    print('main')