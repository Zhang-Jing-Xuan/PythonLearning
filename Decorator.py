import time
import math

def timeCount(func):
    def wrapper(*args):
        t1=time.time()
        res=func(*args)
        t2=time.time()
        print("Total time {:.4} s".format(t2-t1))
        return res
    return wrapper

def isPrime(x):
    if x<2:
        return False
    elif x==2:
        return True
    else:
        for i in range(2,math.ceil(math.sqrt(x)+1)):
            if x%i==0:
                return False
    return True

@timeCount
def printPrime(maxv):
    count=0
    for i in range(2,maxv):
        if isPrime(i):
            print(i)
            count +=1
    return count

count=printPrime(10000)
print(count)