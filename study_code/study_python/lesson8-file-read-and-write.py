#file: read
#>29 file read all as single string
with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents)
    print(contents.rstrip())
file_path = '/home/brucechen/personal/code/beta/study_code/study_python/pi_digits'
with open(file_path) as file_object:
    print('test')
#>30 file read line by line
file_name = 'pi_digits'
with open(file_name) as file_object:
    for line in file_object:
        print(line.strip())
#>31 file read line by line as a list
file_name = 'pi_digits'
with open(file_name) as file_object:
    lines = file_object.readlines()
for line in lines:
    print(line.strip())
#>32 file use file contents
file_name = 'pi_digits'
with open(file_name) as file_object:
    lines = file_object.readlines()
pi_string = ''
for line in lines:
    pi_string += line.strip()
print(pi_string)
birthday = input('please input your birthday')
if birthday in pi_string:
    print('YES')
else:
    print('NO')

#>file: write
#>33 file write to empty file_name
#'r': read-only 'w': empty-write 'a': append-write 'r+': r+w
filename = 'lesson8_file_write.txt'
with open(filename,'a') as file_object:
    file_object.write("I love programming!")
    file_object.write("I love goint to gym!")
