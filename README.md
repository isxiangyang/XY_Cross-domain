# How to use?
python main.py
# GUI
![image](https://user-images.githubusercontent.com/97659869/160229148-7918b0f4-ca3a-4797-8cc6-aeb42289c285.png)

# 主要功能
配合使用工具(如Mimikatz)扫描本地密码，并将密码写入source/pass_list.txt

工具(1)检测域。 检测到域后，工具(2)自动使用 “net user /domain”等语法检测判断域用户

工具(3)探索其他存活域主机：自动将网段IP信息写入source/ip_list.txt)
语法：for /L %I in (1,1,254) DO @ping -w 1 -n 1 192.168.3.%I |findstr "TTL="

工具(4)将本机wifi密码并输出至屏幕

工具(5)进行尝试进行Net use 爆破连接
#Net Use is used to connect to the target host
#net use \\IPADDRESS\ipc$ PASSWORD /user:USERNAME
#SUCH AS:net use \\127.0.0.1\ipc$ admin@123 /user:administrator

工具(6)集成psexec.exe尝试使用已知密码信息进行交叉式爆破获取shell

工具(7)进行多线程扫描端口
