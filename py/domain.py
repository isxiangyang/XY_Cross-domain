# Use ipconfig /all to check whether the content contains domain-related content
import os
def domain():
    cmd="ipconfig /all"
    result=os.popen(cmd)
    result_arry=list(result)
    try:
        print("The domain has been detected：\n")
        result_arry[4][37]
        domain=result_arry[4][36:]
    except:
        domain="No domain detected"
    return domain

