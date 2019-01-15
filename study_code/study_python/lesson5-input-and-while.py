#>18 input()
message = input('please input something: ')
#>19 int()
age = '19'
age = int(age)
print(age)
#>20 while sentence
#example 1
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1
#example 2  bool active
active = True
while active:
    message = input('please input something: ')
    if message == 'quit':
        active = False
    else:
        print(message)
#example 3 break
while True:
    city = input('please input something: ')
    if city == 'quit':
        break
    else:
        print(city)
#example 4 continue
current_number = 0
while current_number <= 10:
    current_number += 1
    if current_number % 2 ==0:
        continue
    print(current_number)
#example 5 move memebers between two lists
unconfirmed_users = ['alice','brian','michael']
confirmed_users = []
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    confirmed_users.append(current_user)
#example 6 delete mutiple same members in a list
pets=['cat','dog','cat','rabbit','cat']
while 'cat' in pets:
    pets.remove('cat')
print(pets)
