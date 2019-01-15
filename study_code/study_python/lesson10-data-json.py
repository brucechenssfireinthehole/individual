#json is a module
#filename.json is a datatype
#>36 json.dump()
import json
numbers = [2,3,5,7,11,13]
filename = 'number.json' #write to this file
with open(filename,'w') as f_obj:
    json.dump(numbers,f_obj)
#>37 json.load()
import json
filename = 'number.json' #read from this file
with open(filename) as f_obj:
    numbers = json.load(f_obj)
print(numbers)

# example 1
import json
#if the username has been stored, then load it; else remind user to add username
filename = 'username.json'
try:
    with open(filename) as f_obj:
        username = json.load(f_obj)
except FileNotFoundError:
    username = input('pleas input your name')
    with open(filename,'w') as f_obj:
        json.dump(username,f_obj)
        print('we will remember your name')
else:
    print('welcome back, ' + username + ' !')

#example 2 : refine the code structure
import json
def get_stored_username():
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    username = input('please input you name')
    filename = 'username.json'
    with open(filename,'w') as f_obj:
        json.dump(username,f_obj)
    return username

def greet_user():
    username = get_stored_username()
    if username:
        print('welcome back '+ username)
    else:
        username = get_new_username()
        print('we will remember your name')
greet_user()
