# JSON is commonly used with data APIS. Here how we can parse JSON into a Python dictionary

import json

#sample JSON 
userJSON = '{"first_name": "John", "last_name": "Doe", "age": 30}'

# Parse to dict
user = json.loads(userJSON)

print(user)

print(user['first_name'])

# Turn Dict to JSON

car = {'make': 'Ford', 'model': 'Mustang', 'year': 1970}

carJSON = json.dumps(car)
print(carJSON)
