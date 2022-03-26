# How to use?
python main.py
# 主要功能
1. 配合使用工具(如Mimikatz)扫描本地密码，并将密码写入source/pass_list.txt  
2. 工具(1)检测域。 检测到域后，自动使用 “net user /domain”等语法检测判断域用户  
3. 工具(3)自动将网段IP信息写入source/ip_list.txt) 
4. 工具(4)集成了PsExec.exe,自动进行横向域爆破式连接
5. Use tool 6 to get target DOS
6. Use tool 7 to search port that you want
