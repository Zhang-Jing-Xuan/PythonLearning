cars=['audi','bmw','subaru','toyota']
for i in cars:
    if i=='bmw':
        print(i.title())
    else:
        print(i.upper())
car='bmw'
a=car=='bmw'
print(a)
b=car=='audi'
print(b)
c=car=='Bmw'#区分大小写
print(c)
a=[1,2,3,4,5,7,7]
print(1 in a)
print(7 in a)
age=12
if age<=4:
    print("Your admission cost is $0.")
elif age<=18:
    print("Your admission cost is $5.")
else:
    print("Your admission cost is $10.")
requested_toppings=['mushrooms','green peppers','extra cheese']
for requested_topping in requested_toppings:
    if requested_topping=='green peppers':
        print("Sorry, we are out of green peppers right now.")
    eles:\
        print("Adding "+requested_topping+'.')
print('\nFinished making your pizza!')
wo='hao kan'
print("Is wo == 'hao kan'? I predict True.")
print(wo == 'hao kan')
print("\nIs wo == 'yi ban hao kan'? I predict False.")
print(wo == 'yi ban hao kan')
