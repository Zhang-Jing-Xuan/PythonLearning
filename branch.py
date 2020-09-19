#guess=eval(input())
'''
if guess==99:
    print("猜对了")
else :
    print("猜错了")
'''
#print("猜{}了".format("对"if guess== 99 else "错"))

'''
if guess>60 or guess==60:
    print("pass")
elif guess>=50:
    print("fail")
else :
    print("bad")
'''
try :
    num=eval(input("请输入一个整数"))
    print(num**2)
except NameError:
    print("不是整数")
