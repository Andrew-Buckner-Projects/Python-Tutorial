# A module is basically a file containing a set of functions to include in your application. There are core python modules, modules you can install using the pip package manager (including Django) as well as custom modules

#import a core module
import datetime

# today = datetime.date.today()

# print(today)

# Just import Date
# from datetime import date
# today = date.today()

# print(today)

# import time
# timestamp = time.time()

# print(timestamp)

# from camelcase import CamelCase

# c = CamelCase()
# print(c.hump('hello there world'))

# Import custom module
import validator
from validator import validate_email

email = 'test@test.com'
if validate_email(email):
    print("Email is valid")
else:
    print('Email is bad')
