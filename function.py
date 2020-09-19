'''
ans=1
def fact(n,m=1):
    global ans
    for i in range(1,n+1):
        ans*=i
    return ans,ans//m,n,m
print(fact(5,3))
'''

'''
f=lambda x,y:x+y
print(f(10,15))
'''
def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)
print(fact(5))
