import os
def get_cmd():
    os.system("net use")
    IPADDR=input("Select an IP address from above to obtain the target DOS:\n")
    exec="py\PSTools\psexec \\\\{IPADDR} -s cmd".format(IPADDR=IPADDR)
    os.system(exec)