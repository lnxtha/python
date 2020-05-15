import pyperclip

name = 'Al'
age = '4000' 
print(f'My name is {name}. Next year I will be {age}.')

a = ['a','b','c']

print(a.sort())

print(name.upper())

print(name.upper().isupper())

print(name.lower().islower())

print(age.isdecimal())
print('allarey'.title())

pyperclip.copy('hello')
print(pyperclip.paste('hello'))
