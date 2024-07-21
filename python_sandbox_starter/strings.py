# Strings in python are surrounded by either single or double quotation marks. Let's look at string formatting and some string methods

name = 'Andrew'
age = 35

#concatenate
print('Hello my name is ' + name + ' and I am ' + str(age))

# String Formatting

# Arguments by position
print('My name is {name} and I am {age}'.format(name = name, age = age))

# F - Strings
print(f'Hello, My name is {name} and I am {age}')

# String Methods

s = 'hello world'

# Capitalize string
print(s.capitalize())
# Swar Cases
print(s.swapcase())

print(len(s))

print(s.split())

