import os
from py.domain import domain
from py.find_other_ip import find_other_ip
from py.wifi import check_wifi
from py.burst import main
from py.port_burst import search_port
from py.get_cmd import get_cmd

print('''
      _                                           
     (_)                                          
__  ___  __ _ _ __   __ _ _   _  __ _ _ __   __ _ 
\ \/ / |/ _` | '_ \ / _` | | | |/ _` | '_ \ / _` |
 >  <| | (_| | | | | (_| | |_| | (_| | | | | (_| |
/_/\_\_|\__,_|_| |_|\__, |\__, |\__,_|_| |_|\__, |
                     __/ | __/ |             __/ |
                    |___/ |___/             |___/ 
   ''')
def display():
    print("___________xy域内横向渗透辅助工具_____________")
    print("1.Checks whether a domain exists")
    print("2.Detects intra-domain users")
    print("3.Check IP addresses of live hosts in the network segment")
    print("4.View the WIFI password of the local PC")
    print("5.Net use blasting connection")
    print("6.Get target DOS")
    print("7.Search port")
    print("h.help")
    print("q.quit")
    print("Enter the number of the command you want to execute and press Enter to continue...")
    print("_____________________________________")
if __name__=="__main__":
    display()
    while True:
        c = input(">>>")
        if c=='1':
            print(domain())
        if c=='2':
            print("In the research and development..But you can use DOS order:net view /domain")
        if c=='3':
            find_other_ip()
        if c=='4':
            check_wifi()
        if c=='5':
            print("Before using Tool 4, use tool 2 to detect live hosts, intercept local passwords with other tools, and write them into dictionary directories  \n")
            print("Blasting for you to connect to the target host, please wait for the error message!  ")
            main()
        if c=='6':
            get_cmd()
        if c=='7':
            search_port()
        if c=="":
            display()
        if c=='h':
            print("""
            1.  Scan local passwords with a tool such as Mimikatz and write the passwords to source/pass_list.txt 
            2.  Use tool 1 to detect the domain.  After the domain is detected, you can use net user /domain to detect the domain user 
            3.  Use tool 3(automatically write network segment IP information to source/ip_list.txt) 
            4.  Connect the lateral burst connection using tool 4
            5.  Use tool 6 to get target DOS
            6.  Use tool 7 to search port that you want
            """)
        if c=='q':
            exit(0)







