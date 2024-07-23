# A class is like a blueprint for creating objects. An object has properties and methods(functions) associated with it. Almost everything in Python is an object

# create class
class User:
    # Constructor
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age

    def greeting(self):
        return f'My name is {self.name} and I am {self.age} years old.'
    
    def has_birthday(self):
        self.age += 1

# Extend class
class Customer(User):
    #Constructor
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
        self.balance = 0

    def set_balance(self, balance):
        self.balance = balance

    def greeting(self):
        return f'My name is {self.name} and I am {self.age} years old with a balance of {self.balance} dollars.'

# Init user object
brad = User('Brad Traversy', 'test@gmail.com', 37)
brad.has_birthday()
print(brad.greeting())

#Init customer object
janet = Customer('Janet Jahnson', 'janet@yahoo.com', 25)

janet.set_balance(500)
print(janet.greeting())