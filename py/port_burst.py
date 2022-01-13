# _*_coding:utf-8 _*_
# @Time    : 2021/12/29/12::16
# @Author  : xiangyang


import socket
import threading
import time

start_time=time.time()
def main(target):
    print('Start:')
    for port in range(1,636600):
        t=threading.Thread(target=hackport,args=(target,port))
        t.start()
def hackport(target,port):
    try:
        res = socket.socket()
        res.connect((target,port))
        print(target,port)
        res.close()
    except:
        pass
def search_port():
    target=input("Please enter the ip you want:")
    main(target)
    end_time=time.time()
    print("Spend time：",end_time-start_time,"s")


