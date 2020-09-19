for i in range(4):
    print("Hi")
for i in range(1,6,2):
    print(i)
for i in [123,"PY",456]:
    print(i,end=",")
i=3
while i>0:
    i-=1#Control C终止
    print(i)
s="python"
while s!="":
    for c in s:
        print(c,end="")
    s=s[:-1]
