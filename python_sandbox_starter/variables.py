# A variable is a container for a value, which can be of various types

'''
This is a 
multiline comment
or docstring (used to define a functions purpose)
can be single or double quotes
'''

"""
VARIABLE RULES:
  - Variable names are case sensitive (name and NAME are different variables)
  - Must start with a letter or an underscore
  - Can have numbers but can not start with one
"""

#x = 1           # Int
#y = 2.5         # Float
#name = 'john'   # string
#is_cool = True  # bool

#Multiple Assignment
x, y, name, is_cool = (1, 2.5, 'john', True)

print(x, y, name, is_cool)

#basic Math

a = x + y
print(a)
print(type(a))

# Casting

x = str(x)
print(type(x), x)
