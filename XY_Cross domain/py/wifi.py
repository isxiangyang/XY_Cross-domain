import os
def check_wifi():
    def check_name():
        name_result = os.popen("netsh wlan show profiles")
        for i in list(name_result):
            print(i.replace("\n",""))
    def show_password():
        print("------------------------------------------------xy专用---------------------------------------------------------------------")
        print("""
        
                         [---------------------------------------------]
        All WIFI information is listed above, please find the WIFI name and continue to enter  ：
                         [---------------------------------------------]
    \n
        """)
        name_password = os.popen('netsh wlan show profiles name="{wifi_name}" key=clear'.format(wifi_name=input("Please enter the name of WIFI to query:\n")))
        for i in list(name_password):
            print(i)
        print("Passwords listed\n！")
    check_name()
    show_password()