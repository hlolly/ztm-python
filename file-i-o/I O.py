# I/O - INPUT / OUTPUT

my_file = open('test.txt')

print(my_file.read())

# ONLY POSSIBLE TO READ A FILE ONCE LIKE THIS

my_file.seek(0)
print(my_file.read())

my_file.seek(0)
print(my_file.readline())
print(my_file.readline())

my_file.seek(0)
print(my_file.readlines())

my_file.close()

with open('test.txt', mode='r+') as my_file:
    text = my_file.write('Hey! It\'s me')
    print(text)

with open('test.txt', mode='a') as my_file:
    text = my_file.write(' :)')
    print(text)

# mode = w - rewrite everything or create a new file

with open('sad.txt', mode='w') as my_file:
    text = my_file.write(':(')
    print(text)

# To open a file in another folder : open(foldername\file.txt)
# ABSOLUTE PATH: C:\Users\patri\Desktop\foldername\file.txt
# Current folder: .\foldername\file.txt
# Back a folder: ..\foldername\file.txt

# Check pathlib

# ERRORS

try:
    with open('hi.txt', mode='r') as my_file:
        print(my_file.read())
except FileNotFoundError as err:
    print('File does not exist')
except IOError as err:
    print('IO error')

