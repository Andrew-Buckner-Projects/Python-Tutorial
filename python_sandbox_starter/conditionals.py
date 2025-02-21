# If/ Else conditions are used to decide to do something based on something being true or false

x = 13
y = 7


# Comparison Operators (==, !=, >, <, >=, <=) - Used to compare values

# Simple If
if x > y:
    print(f'{x} is greater then {y}')

#if / else
if x > y:
    print(f'{x} is greater then {y}')
else:
    print(f'{y} is greater or = to {x}')

# elif
if x > y:
    print(f'{x} is greater then {y}')
elif x == y:
    print(f'{y} is  = to {x}')
else:
    print(f'{y} is greater than {x}')



# Logical operators (and, or, not) - Used to combine conditional statements

#and
if x > 2 and x <= 10:
    print(f'{x} is in range 3-10')

#not
if not(x==y):
    print(f'{x} not equal to {y}')

# Membership Operators (in, not in) - Membership operators are used to test if a sequence is presented in an object

numbers = [1,2,3,4,5]

#in
if x in numbers:
    print(x in numbers)

# not in
if x not in numbers:
    print(x not in numbers)


# Identity Operators (is, is not) - Compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:

#is
if x is y:
    print(x is y)

#is not
if x is not y:
    print(x is not y)




