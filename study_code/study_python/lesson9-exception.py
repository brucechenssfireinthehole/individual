# exception process
#>34 try-except
try:
    print(5/0)
except ZeroDivisionError:
    print('you cannot divide by zero!')
#>35 try-except-else
try:
    print(5/1)
except ZeroDivisionError:
    print('you cannot divide by zero!')
else:
    print('division success!')

# example 1
def count_words(filename):
    """calculate the number of words in file"""
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        msg = "sorry, " + filename + " does not exist"
        print(msg)
    else:
        words = contents.split()
        num_words = len(words)
        print("The words'number is " + str(num_words))
filename = 'alice.txt'
count_words(filename)

#>36 pass: without exception process
try:
    print(5/0)
except ZeroDivisionError:
    pass
else:
    print('division success!')
