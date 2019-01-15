alien_0 = {'color':'green','point':5}
#>16 dict-change/add/delate
alien_0['color'] = 'red'
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)
del alien_0['color']
#example 1
alien_0 = {'x_position':0,'y_position':25,'speed':'medium'}
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else alien_0['speed'] == 'fast':
    x_increment = 3
alien_0['x_position'] = alien_o['x_position'] + x_increment
print('New x-position: is' + str(alient_0['x_increment']))
#>17 traverse directionary
for key,value in alien_0.items():
    print('\nkey:' + str(key))
    print('value:' + str(value))
for key in alien_0.keys():
    print(key.title())
for key in sorted(alien_0.keys()):
    print(key.title())
for value in alien_0.values():
    print(value)
for vaule in set(alien_0.values()): #set(): change members of list to unique
    print(value)
