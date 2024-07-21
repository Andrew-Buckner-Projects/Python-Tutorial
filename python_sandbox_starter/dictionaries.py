# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.
# Read more about dictionaries at https://docs.python.org/3/tutorial/datastructures.html#dictionaries

#create Dict

person = {
    'first_name': 'John',
    'last_name': 'Doe',
    'age': 30
}

print(person, type(person))

#With a constructor
#person2 = dict(first_name = 'Sara', last_name = 'Williams')
#print(person2, type(person2))

#Get value
print(person['first_name'])
print(person.get('last_name'))

#add key.valeu
person['phone'] = '555-555-5555'
print(person)

# Get dict keys
print(person.keys())
print(person.items())

#Coppy a dictionary

person2 = person.copy()
person2['city'] = 'Boston'
print(person2)

#Remove item
del(person['age'])
person.pop('phone')
print(person)

#clear
# person.clear()
# print(person)

#length
print(len(person2))

# List of dictionary
people = [
    {'name': 'Martha', 'age':30},
    {'name': 'Kevin', 'age':25}
]

print(people)

#get name of first person
print(people[1]['name'])