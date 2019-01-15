#>6 list type
bicycles=['trek','cannondale']
print (bicycles)
print(bicycles[0])
#>7 list-change/add/delate
bicycles[0]='change'
bicycles.append("motorcycle")
bicycles.insert(0,"ducati")
del bicycles[0]
pop_bicycle=bicycles.pop()
pop_bicycle=bicycles.pop(0)
bicycles.remove('cannondale')
#>8 list-sort()
cars=['bmw','audi','toyota','subaru']
cars.sort() #forever sort as the abc sorts.
print(cars)
cars.sort(reverse=True)
print(cars)
print(sorted(cars)) #temporary sort as the abc sorts
cars.reverse() #sort as the reverse direction
len(cars) #get the length of a list
#>9 traverse list
magicians=['alice','bob','bruce']
for magician in magicians:
    print(magician)
    print(magician.title()+" is so good!\n")
#>10 number list
for value in range(1,5):  # create a series of numbers ,not a list
    print(value)  # 1 2 3 4 stop before 5
numbers = list(range(1,5)) #create a number-list with list() and range()
print(numbers)
even_numbers=list(range(1,2,10))
print(even_numbers)
squares=[]
for value in range(1,11):
    squares.append(value**2)
print(squares)
squares = [value**2 for value in range(1,11)] #creat a number-list by one line
min(numbers) #minimun in number-list
max(numbers) #maximun in number-list
sum(numbers) #sum of a number- list
#>11 list slice
players=['charles','martina','michhael','florence','eli']
print(players[0:4]) # print 0 1 2 3
print(players[1:]) # print 1 2 3 4
print(players[:3]) # print 0 1 2
print(players[-3:]) # print 2 3 4
print(plyaers[:]) # print all
#>12 traverse list-slice
for player in players[0:3]:
    print(player)
#>13 copy a list by slice
girls=player[:]

#>14 tuple type: similar with list but whose members cannot be revised,
# tuple itself can be revised
dimensions=(100,50)
dimensions=(200,100)
