users_name = input("Hello! Please Enter your name: ")
birthday_month = input ("Enter the month you were born in: ")

print(f'Hello {users_name}')

letters_in_name = len(users_name)

print(f'You have ' + str(letters_in_name) + ' letters in your name')

if birthday_month.lower() == 'august':
    print('Happy birthday month!')
else:
    print('Your birthday month is ' + birthday_month + '.')
