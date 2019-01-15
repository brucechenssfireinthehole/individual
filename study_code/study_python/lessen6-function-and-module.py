#>21 function hello
def greet_user():
    """say hello"""
    print('hello')
greet_user()

def greet_user2(username):
    """say hello of username"""
    print('hello '+ 'username')
greet_user2('bruce chen')
#>22 function parameter input: postion/keywords/default
def describe_pet(pet_name, animal_type='dog'):
    print('\nI have a '+animal_type + ".")
    print("It's name is "+'pet_name')
describe_pet('willie')
describe_pet(pet_name='willie')
describe_pet('harry','hamster')
describe_pet(pet_name='harry',animal_type='hamster')
describe_pet(animal_type='hamster',pet_name='harry')
#>23 function return
def get_full_name(first_name,last_name):
    full_name = first_name+' '+last_name
    return full_name.title()
my_name = get_full_name('bruce','chen')
print(my_name)
#>24 function optional parameter input
def get_full_name(first_name,last_name,middle_name=''):
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' +last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()
#>25 function parameter input : list
def print_models(unprinted_list,printed_list):
    print('do nothing')
print_models(unprinted_list,printed_list)
print_models(unprinted_list[:],printed_list) #input the copy list of unprinted_list
#>25 function parameter input: *tuple
def make_pizza(*toppings):
    print(toppings)

make_pizza('mushrooms')
make_pizza('mushrooms','cheese')
#>26 function parameter input: **dictionary
def build_profile(first,last,**user_info):
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key,value in user_info:
        profile[key] = value
    return profile
user_profile = build_profile('bruce','chen',
                            location='shanghai',
                            field='AI graphics')
print(user_profile)

#>27 function module import
import module_file
module_file.function_name()
from module_file import funciton_name
from module_file import function_name_1,function_name_2,function_name_3
function_name()
import module_file as m
m.funtion_name()
from module_file import function_name as mp
mp()
from module_file import * #import all funciton from module
