import pandas as pd
import numpy as np

'''
s=pd.Series([1,3,6,np.nan,44,1])
print(s)
dates=pd.date_range('20200828',periods=6)
print(dates)
df=pd.DataFrame(np.random.randn(6,4),index=dates,columns=['a','b','c','d'])
print(df)
df1=pd.DataFrame(np.arange(12).reshape((3,4)))
print(df1)
df2=pd.DataFrame({'A':1.,
                  'B':pd.Timestamp('20200828'),
                  'C':pd.Series(1,index=list(range(4)),dtype='float32'),
                  'D':np.array([3]*4,dtype='int32'),
                  'E':pd.Categorical(["test","train","test","train"]),
                  'F':'fool'})
print(df2)
print(df2.dtypes)
print(df2.index)
print(df2.columns)
print(df2.values)
print(df2.describe())
print(df2.T)
print(df2.sort_index(axis=1,ascending=False))#按列名称排序
print(df2.sort_index(axis=0,ascending=False))#按行名称排序
print(df2.sort_values(by='E'))
'''

'''
dates=pd.date_range('20200828',periods=6)
df=pd.DataFrame(np.arange(24).reshape((6,4)),index=dates,columns=['A','B','C','D'])
print(df)
print()
#print(df['A'],df.A)
#print(df[0:3],df['20200829':'20200831'])

#select by label:loc
print(df.loc['20200829'])
print(df.loc[:,['A','B']])
print()
print(df.loc['20200829',['A','B']])
#select by position:iloc
print(df)
print()
print(df.iloc[3])#第3行
print(df.iloc[3,1])#第3行第1位
print(df.iloc[3:5,1:3])
print(df.iloc[[1,3,5],1:3])#第1，3，5行;第1，2列
#Boolean indexing
print(df)
print(df[df.A >8])
'''

'''
dates=pd.date_range('20200829',periods=6)
df=pd.DataFrame(np.arange(24).reshape((6,4)),index=dates,columns=['A','B','C','D'])
df.iloc[2,2]=1111
df.loc['20200829','B']=2222
df.A[df.A>4]=0
print(df)
df['F']=np.nan
df['E']=pd.Series([1,2,3,4,5,6],index=pd.date_range('20200829',periods=6))
print(df)
'''


'''
dates=pd.date_range('20200829',periods=6)
df=pd.DataFrame(np.arange(24).reshape((6,4)),index=dates,columns=['A','B','C','D'])
df.iloc[0,1]=np.nan
df.iloc[1,2]=np.nan

print(df)
print(df.dropna(axis=0,how='any'))#丢掉行,出现任何一个nan就把整行丢掉(默认)
print(df.dropna(axis=0,how='all'))#丢掉行，只有该行所有元素全都是nan才把整行丢掉

print(df.fillna(value=0))
print(df.isnull())

print(np.any(df.isnull())==True)#有一个为nan就输出True
'''

'''
data=pd.read_csv('student.csv')
print(data)
data.to_pickle('student.pickle')
'''


'''
#concatenating
df1=pd.DataFrame(np.ones((3,4))*0,columns=['a','b','c','d'])
df2=pd.DataFrame(np.ones((3,4))*1,columns=['a','b','c','d'])
df3=pd.DataFrame(np.ones((3,4))*2,columns=['a','b','c','d'])
res=pd.concat([df1,df2,df3],axis=0)#竖向合并
res=pd.concat([df1,df2,df3],axis=0,ignore_index=True)#竖向合并
print(res)

#join,['inner','outer']
df1=pd.DataFrame(np.ones((3,4))*0,columns=['a','b','c','d'],index=[1,2,3])
df2=pd.DataFrame(np.ones((3,4))*1,columns=['b','c','d','e'],index=[2,3,4])
res=pd.concat([df1,df2])#没有的用nan填充(默认outer)
res=pd.concat([df1,df2],join='inner')#将相同的合并，其他裁剪掉
res=pd.concat([df1,df2],join='inner',ignore_index=True)#将相同的合并，其他裁剪掉
print(res)

#append
df1=pd.DataFrame(np.ones((3,4))*0,columns=['a','b','c','d'])
df2=pd.DataFrame(np.ones((3,4))*1,columns=['a','b','c','d'])
df3=pd.DataFrame(np.ones((3,4))*1,columns=['a','b','c','d'],index=[2,3,4])
res=df1.append([df2,df3],ignore_index=True)
#res=df1.append([df2,df3])
print(res)

df1=pd.DataFrame(np.ones((3,4))*0,columns=['a','b','c','d'])
s1=pd.Series([1,2,3,4],index=['a','b','c','d'])
res=df1.append(s1,ignore_index=True)
print(res)
'''

'''
#merge
left=pd.DataFrame({'key':['K0','K1','K2','K3'],
                   'A':['A0','A1','A2','A3'],
                   'B':['B0','B1','B2','B3']})
right=pd.DataFrame({'key':['K0','K1','K2','K3'],
                   'C':['C0','C1','C2','C3'],
                   'D':['D0','D1','D2','D3']})
print(left)
res=pd.merge(left,right,on='key')
print(res)

left=pd.DataFrame({'key1':['K0','K0','K1','K2'],
                   'key2':['K0','K1','K0','K1'],
                   'A':['A0','A1','A2','A3'],
                   'B':['B0','B1','B2','B3']})
right=pd.DataFrame({'key1':['K0','K1','K1','K2'],
                    'key2':['K0','K0','K0','K0'],
                   'C':['C0','C1','C2','C3'],
                   'D':['D0','D1','D2','D3']})
print(left)
print(right)
#how=['left','right','outer','inner']
res=pd.merge(left,right,on=['key1','key2'])#默认how='inner'
res=pd.merge(left,right,on=['key1','key2'],how='outer')
print(res)
#indicator
df1=pd.DataFrame({'col1':[0,1],'col_left':['a','b']})
df2=pd.DataFrame({'col1':[1,2,2],'col_right':[2,2,2]})
print(df1)
print(df2)
res=pd.merge(df1,df2,on='col1',how='outer',indicator=True)#显示如何合并
res=pd.merge(df1,df2,on='col1',how='outer',indicator='indicator_column')
print(res)
#index
left=pd.DataFrame({'A':['A0','A1','A2'],
                   'B':['B0','B1','B2']},
                   index=['K0','K1','K2'])
right=pd.DataFrame({'C':['C0','C2','C3'],
                   'D':['D0','D2','D3']},
                   index=['K0','K2','K2'])
print(left)
print(right)
res=pd.merge(left,right,left_index=True,right_index=True,how='outer')
print(res)

#overlapping
boys=pd.DataFrame({'k':['K0','K1','K2'],'age':[1,2,3]})
girls=pd.DataFrame({'k':['K0','K1','K2'],'age':[4,5,6]})
print(boys)
print(girls)
res=pd.merge(boys,girls,on='k',suffixes=['_boy','_girl'],how='inner')
print(res)
'''









