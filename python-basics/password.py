username = input('What is your username? ')
password = input('What is your password? ')

password_length = len(password)
password_hidden = ('*' * password_length)

print(f'{username}, your password {password_hidden} is {password_length} letters long')
