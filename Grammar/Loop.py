a=["Tom","David","Alice"]
for b in a:
    print(b)
for value in range(1,5):
    print(value)
print(list(range(1,5)))
even_numbers=list(range(2,12,2))
print(even_numbers)
squares=[]
for value in range(1,11):
    squares.append(value**2)
print(squares)
squares=[value**2 for value in range(1,11)]
print(squares)
print(squares[0:3])
print(squares[0:2])
print(squares[:4])
print(squares[2:])
print(squares[-3:])
players = ['charles','martina','michael','florence','eli']
print('Here are the first three players on my team: ')
for player in players[:3]:
    print(player.title())
a=[0,1,2,3]
b=a
a.append(4)
b.append(5)
print(a)
print(b)
dimensions=(200,500,1)
print(dimensions)
print(dimensions[1])
print(dimensions[0])

for dimension in dimensions:
    print(dimension)

dimensions=(10,20,30)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)
creatures=['我','你','他']
for creature in creatures:
    print(creature)

for creature in creatures:
    print(creature+'爱吃披萨！')

print('大家都爱吃披萨！')
