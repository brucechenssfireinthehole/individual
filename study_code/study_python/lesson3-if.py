#>15 if sentence
#example 1
cars=['audi','bmw','subaru','toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())
#example 2
cars=['audi','bmw','subaru','toyota']
if 'audi' not in cars:
    print('there is none of mine')
    mark = False
else:
    print('I have the car')
    mark = True
#example 3
age = 12
if age < 4:
    print('section1')
elif age < 18:
    print('seciont2')
else:
    print('section3')
#example 4 if and list
requests = []
if requests:
    for request in requests:
        print(request)
else:
    print('there is no request')
