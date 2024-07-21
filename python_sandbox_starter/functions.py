# A function is a block of code which only runs when it is called. In Python, we do not use parentheses and curly brackets, we use indentation with tabs or spaces

#creat a function
def sayHello(name = 'Forgot to enter'):
    print(f'Hello {name}')

sayHello('John Doe')
sayHello()

#return Values
def getSum(num1, num2):
    total = num1 + num2
    return total

num = getSum(3,4)
print(num)

# Lambda function

getSum = lambda num1, num2 : num1 + num2
print(getSum(10,3))



# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression. Very similar to JS arrow functions

