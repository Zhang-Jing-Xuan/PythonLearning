import numpy as np

'''
def npSum():
    a=np.array([0,1,2,3,4])
    b=np.array([9,8,7,6,5])
    c=a**2+b**3
    return c
#print(npSum())
'''

'''
a=np.array([[0,1,2,3,4],
            [9,8,7,6,5]])
print(a)
print('number of dim:',a.ndim)
print('shape:',a.shape)
print('size:',a.size)
print(a.dtype)
print(a.itemsize)
'''

#a=np.array([2,23,4],dtype=np.double)
#print(a.dtype)

'''
a=np.array([ [2,23,4],
           [2,43,4] ])
print(a)

a=np.zeros( (3,4) )
print(a)

a=np.ones( (3,4),dtype=np.int16 )
print(a)

a=np.empty( (3,4))
print(a)

a=np.arange(10,20,2)
print(a)

a=np.arange(12).reshape((3,4))
print(a)

a=np.linspace(1,10,6).reshape((2,3))
print(a)
'''


'''
a=np.array([10,20,30,40])
b=np.arange(4)
print('a,b=',a,b)
c=a-b
print('c=',c)
c=10*np.sin(a)
print(c)

print(b<3)
print(b==3)


a=np.array([[1,1],
            [0,1]])
b=np.arange(4).reshape((2,2))
print(a)
print(b)
c=a*b#逐个相乘
print(c)
c=np.dot(a,b)#矩阵乘法
c=a.dot(b)#功能同c=np.dot(a,b)
print(c)

a=np.random.random((2,4))
print(a)
#axis=0:列    axis=1:行
print(np.sum(a,axis=1))
print(np.min(a,axis=0))
print(np.max(a))
'''


'''
A=np.arange(14,2,-1).reshape((3,4))

print(np.argmin(A))#A最小值索引
print(np.argmax(A))

print(np.mean(A))#A的平均值
print(A.mean())#功能同print(np.mean(A))
print(np.median(A))#A的中位数
print(A)
print(np.cumsum(A))#A的累加
print(np.diff(A))#A的累差
print(np.nonzero(A))#A的非零数(行数，列数)
print(np.sort(A))#逐行排序
print(np.transpose(A))#A的转置
print((A.T).dot(A))
print(np.clip(A,5,9))#所有大于9的数变成9，所有小于5的数变成5
print(A)
print(np.mean(A,axis=0))
'''

'''
A=np.arange(3,15)
print(A)
print(A[3])
A=np.arange(3,15).reshape((3,4))
print(A)
print(A[2])
print(A[1][1])
print(A[2,1])#功能同print(A[2][1])
print(A[2,:])#第2行的所有数
print(A[:,1])#第1列的所有数
print(A[1,1:2])#第1行下标为[1,2)的数

for row in A:#迭代行
    print(row)
for column in A.T:#迭代列
    print(column)
print(A.flatten())
for item in A.flat:#迭代A中的每一项
    print(item)
'''


'''
A=np.array([1,1,1])
B=np.array([2,2,2])


print(np.vstack((A,B)))#上下合并(vertical stack)
C=np.vstack((A,B))
D=np.hstack((A,B))#左右合并
print(D)
print(A.shape,C.shape,D.shape)

print(A[np.newaxis,:])#在行上加了一个维度
print(A[:,np.newaxis])#在列上加了一个维度

A=np.array([1,1,1])[:,np.newaxis]
B=np.array([2,2,2])[:,np.newaxis]
D=np.hstack((A,B))#左右合并
print(D)

print(A)
print(B)
C=np.concatenate((A,B,B,A),axis=0)
print(C)
'''

'''
A=np.arange(12).reshape((3,4))
print(A)

print(np.split(A,2,axis=1))#把4列分成2块
print(np.split(A,3,axis=0))#把3行分成3块
print(np.array_split(A,3,axis=1))#把4列分成不等的3块
print(np.vsplit(A,3))#纵向分割
print(np.hsplit(A,2))#横向分割
'''


a=np.arange(4)
print(a)
b=a
c=a
d=b
a[0]=11
print(a)
print(b is a)
print(b)
print(d is a)
d[1:3]=[22,33]
print(d)
print(a)
b=a.copy()#deep copy仅仅把a的值赋给b但没有关联a与b
a[3]=44
print(a)
print(b)





