#0301 列表
bicycles=['trek','cannondale','redline','specialized']
print(bicycles)
#
#访问列表元素
print(bicycles[0])
print(bicycles[1])
print(bicycles[3])
print(bicycles[-1])

#使用列表中的各个值
message='my first bicycle was a '+bicycles[0].title()+'.'
print(message)

##修改列表元素
motorcycles=['honda','yamaha','suzuki']
print(motorcycles)

motorcycles[0]='ducati'
print(motorcycles)
#添加列表元素
motorcycles.append('ducati')#在末尾处添加
print(motorcycles)
motorcycles.insert(0,'ducati')#在0位添加
print(motorcycles)

#先创建空列表，后向里面添加元素
motorcycles=[]
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)
#列表删除元素
del motorcycles[0]
print(motorcycles)
#Pop()函数，弹出列表中最后的元素

motorcycles=['a','b','c']
print(motorcycles)
#所以一般执行这个函数的时候就要赋值，才能将踢出的元素保存

motorcycles.pop()
print(motorcycles)

poped_motorcycles=motorcycles.pop()
print(motorcycles)
print(poped_motorcycles)

motorcycles=['honda','ymaha','suzuki']
last_owned=motorcycles.pop()
print('The last motorcycle I owoned was a '+last_owned.title()+'.')

#弹出列表中任意位置的元素

first_owned=motorcycles.pop(0)
print('The first motorcycle I owned was a '+first_owned.title()+'.')

#根据值删除元素
motorcycles=['honda','yamaha','suzuki','ducati']
print(motorcycles)
motorcycles.remove('ducati')
print(motorcycles)
#remove删除
too_expensive='suzuki'
motorcycles.remove(too_expensive)
print(motorcycles)
print('\nA '+too_expensive.title()+' is too expensive for me')
motorcycles.remove('honda')
print(motorcycles)

#对列表元素按首字母进行永久性排序
cars=['bmw','audi','toyota','subaru']
cars.sort()
print(cars)
#列表元素首字母永久性反序
cars.sort(reverse=True)
print(cars)
#临时排序，调用函数:y=f(x),本身的x没有变；x.f()相当于x=f(x)，x本身变了
print('Here is the ariginal list:')
print(cars)
print('\nHere is the sorted list:')
print(sorted(cars))
print('\nHere is the original list again:')
print(cars)

#倒着打印，倒序打印列表
print(cars)
cars.reverse()
print(cars)
#
#列表长度
print(len(cars))



# 0302习题3-1 姓名列表，访问元素，打印出来
onepiece=['Monkey·D·Luffy','Roronoa Zoro','Nami','Usopp','Sanji'
,'Tony-Tony Chopper','Nico Robin','Franky','Brook','Jinbe','Carrot']

print(onepiece[0])
print(onepiece[1])
print(onepiece[2])
print(onepiece[3])
print(onepiece[4])
print(onepiece[-6])
print(onepiece[-5])
print(onepiece[-4])
print(onepiece[-3])
print(onepiece[-2])
print(onepiece[-1])


# 0302习题3-2 姓名列表，打印人名+问候语
print("Love you，"+onepiece[0])
print("Love you，"+onepiece[1])
print("Love you，"+onepiece[2])
print("Love you，"+onepiece[3])
print("Love you，"+onepiece[4])
print("Love you，"+onepiece[-6])
print("Love you，"+onepiece[-5])
print("Love you，"+onepiece[-4])
print("Love you，"+onepiece[-3])
print("Love you，"+onepiece[-2])
print("Love you，"+onepiece[-1])

# 0302 习题3-3 通勤方式列表，打印一些列有关通勤方式的宣言
transport=["大妈",'路飞','leijiu']
print(transport[0]+'是我的最最理想型')

# 0302 习题3-4 邀请晚宴名单 发出邀请
onepiece=['Monkey·D·Luffy','Roronoa Zoro','Nami','Usopp','Sanji'
,'Tony-Tony Chopper','Nico Robin','Franky','Brook','Jinbe','Carrot']

print("Welcome to the wedding, "+onepiece[0])
print("Welcome to the wedding, "+onepiece[1])
print("Welcome to the wedding, "+onepiece[2])
print("Welcome to the wedding, "+onepiece[3])
print("Welcome to the wedding, "+onepiece[4])
print("Welcome to the wedding, "+onepiece[-6])
print("Welcome to the wedding, "+onepiece[-5])
print("Welcome to the wedding, "+onepiece[-4])
print("Welcome to the wedding, "+onepiece[-3])
print("Welcome to the wedding, "+onepiece[-2])
print("Welcome to the wedding, "+onepiece[-1])


# 习题3-5 修改嘉宾名单
a=onepiece[1]
onepiece.remove(a)
print(a+' cannot come.')
onepiece.append('老鹰记者')
print("Welcome to the wedding, "+onepiece[0])
print("Welcome to the wedding, "+onepiece[1])
print("Welcome to the wedding, "+onepiece[2])
print("Welcome to the wedding, "+onepiece[3])
print("Welcome to the wedding, "+onepiece[4])
print("Welcome to the wedding, "+onepiece[-6])
print("Welcome to the wedding, "+onepiece[-5])
print("Welcome to the wedding, "+onepiece[-4])
print("Welcome to the wedding, "+onepiece[-3])
print("Welcome to the wedding, "+onepiece[-2])
print("Welcome to the wedding, "+onepiece[-1])

# 3-6

onepiece.insert(0,'Germa')
onepiece.insert(4,'Fire Tank')
onepiece.append('Big Mom')
print("Welcome to the wedding, "+onepiece[0])
print("Welcome to the wedding, "+onepiece[1])
print("Welcome to the wedding, "+onepiece[2])
print("Welcome to the wedding, "+onepiece[3])
print("Welcome to the wedding, "+onepiece[4])
print("Welcome to the wedding, "+onepiece[5])
print("Welcome to the wedding, "+onepiece[6])
print("Welcome to the wedding, "+onepiece[7])
print("Welcome to the wedding, "+onepiece[-6])
print("Welcome to the wedding, "+onepiece[-5])
print("Welcome to the wedding, "+onepiece[-4])
print("Welcome to the wedding, "+onepiece[-3])
print("Welcome to the wedding, "+onepiece[-2])
print("Welcome to the wedding, "+onepiece[-1])

# 3-7
print("\nSorry, there are only two places left")
a=onepiece.pop(-1)
print("The wedding is canceled, franchement desole, "+a)

a=onepiece.pop(-1)
print("The wedding is canceled, franchement desole, "+a)

a=onepiece.pop(-1)
print("The wedding is canceled, franchement desole, "+a)

a=onepiece.pop(-1)
print("The wedding is canceled, franchement desole, "+a)

a=onepiece.pop(-1)
print("The wedding is canceled, franchement desole, "+a)

a=onepiece.pop(-1)
print("The wedding is canceled, franchement desole, "+a)

a=onepiece.pop(-1)
print("The wedding is canceled, franchement desole, "+a)

a=onepiece.pop(-1)
print("The wedding is canceled, franchement desole, "+a)

a=onepiece.pop(-1)
print("The wedding is canceled, franchement desole, "+a)

a=onepiece.pop(-1)
print("The wedding is canceled, franchement desole, "+a)


a=onepiece.pop(-1)
print("The wedding is canceled, franchement desole, "+a)

a=onepiece.pop(-1)
print("The wedding is canceled, franchement desole, "+a)

print(onepiece)

# 对剩下的两位，打印一句话
print('\n有缘千里来相会，雷玖在等你'+onepiece[1])
print('我从远方赶来赴你一面之约'+onepiece[0])

# 删除余下两位

# del onepiece[0]
# del onepiece[1]

print(onepiece)



# 0303 习题 3-8 放眼世界，想出至少5个你想去的地方，顺序打乱
to_the_places_I_belong=['swizerland','my side','higher dimentional space','my home','argentina']

# 打印原始列表
print("The original list:\n")
print(to_the_places_I_belong)
#
# sorted()按字母顺序打印，不改变原来列表的顺序
print("\nSorted list:\n")
print(sorted(to_the_places_I_belong))

# 再次打印确认列表顺序没变
print("\nThe original list again:\n")
print(to_the_places_I_belong)

# sorted()反序，不改变列表原来顺序,reverse=Ture

print("The list after being sorted_reverse=True:\n")
print(sorted(to_the_places_I_belong,reverse=True))

# 再次打印确认列表顺序没变
print("\nThe original list again:\n")
print(to_the_places_I_belong)

#reverse反转，改变原列表的顺序
print('\n用reverse反转的效果\n')
to_the_places_I_belong.reverse()
print(to_the_places_I_belong)

#reverse()再次反转
print("\n用reverse再次反转列表的效果\n")
to_the_places_I_belong.reverse()
print(to_the_places_I_belong)

#sort()改变列表本身的顺序

print('\nThe list after being ordered by sort()\n')
to_the_places_I_belong.sort()
print(to_the_places_I_belong)

#sort()反序


print('\nThe list after being ordered by sort(reverse=Ture)\n')
to_the_places_I_belong.sort(reverse=True)
print(to_the_places_I_belong)


# 0304 习题3-9 哎呀，早说呀，我怎么把len()这个函数给忘了

onepiece=['Monkey·D·Luffy','Roronoa Zoro','Nami','Usopp','Sanji'
,'Tony-Tony Chopper','Nico Robin','Franky','Brook','Jinbe','Carrot']

# print(len(onepiece))


# 0304 习题 3-10 自建列表，尝试使用本章的所有函数

# 1.访问
# 2.修改
# 索引直怼
# print(onepiece)
# onepiece[0]='Charlotte Linlin'
# print(onepiece)

# 3.添加

onepiece.append('Charlotte Linlin')#末尾添加
print(onepiece)
onepiece.insert(0,'Shanks')#根据索引插入
print(onepiece)

# 4.删除
print(onepiece)
del onepiece[2]#根据索引删除，特点是删了就删了，这个值不能给别人
print(onepiece)

a=onepiece.pop(2)
#默认弹出最后一个，特点从列表中弹出，可以给别人
#需要知道索引位置
print(a)
print(onepiece)


a=onepiece.remove('Monkey·D·Luffy')
print(onepiece)
print(a)

# 特点，不知道索引位置，知道元素是什么
# remove出去的元素不可以通过赋值继续使用
# 剩下就是对列表一顿操作的函数，各种排序，上一道题做过了，不想搞了

# 0305 3-11 有意引发错误

list=['a','b','c']
list[0]
a=list.remove('c')