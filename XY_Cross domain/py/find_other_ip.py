#多线程寻找其他存活主机
import os
import threading

arry = []
def find_other_ip():
    def ipconfig():
        os.popen("ipconfig")
    ipadd=input("Please enter the IP  ，such as: 192.168.10.\n")
    print("IP range  :{ipadd}".format(ipadd=ipadd)+"1-254")
    def function(i):
        global arry
        result=os.popen('for /L %I in ({i},254,254) DO @ping -w 1 -n 1 {ipadd}%I |findstr "TTL="'.format(i=i,ipadd=ipadd))
        for ip in list(result):
            if ip != "":
                arry.append(ip.replace("\n",""))
    def find_live():
        for i in range(254):
          rs=threading.Thread(target=function,args=(i,))
          rs.start()
    find_live()
    def main():
        try:
            arry[0]
            print("A live host was detected",len(arry),"\n","Check it out in the source/ IP list.txt file！")
            with open("source/ip_list.txt", "w+", encoding="utf-8") as f:
                for ip_list in arry:
                    final = ip_list[3:-25]+"\n"
                    final=final.replace(" ","")
                    f.write(final)
        except:
            print("In {ipadd}{fw}，No other live hosts were detected！".format(ipadd=ipadd,fw="1-254"))
    while len(threading.enumerate()) > 1:
        pass
    main()





