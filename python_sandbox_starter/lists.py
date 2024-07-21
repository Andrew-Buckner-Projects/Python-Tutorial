# A List is a collection which is ordered and changeable. Allows duplicate members.

# Create lsit

numbers = [1,2,3,4,5]

#  Use a constructor
numbers2 = list((1,2,3,4,5))

print(numbers, numbers2)

fruits = ['Apples', 'Oranges', 'Grapes', 'Pears']

#Get a value
print(fruits[2])

# get length
print(len(fruits))

# appent to list
fruits.append('Mangos')
print(fruits)

# remove stuff
fruits.remove('Grapes')
print(fruits)

#Insert into Position
fruits.insert(2, 'Strawberries')
print(fruits)

#Remove by positin
fruits.pop(2)
print(fruits)

#reverse lsit

fruits.reverse()
print(fruits)

#sort alphabetically
fruits.sort()
print(fruits)

#sort reverse alphabetically
fruits.sort(reverse = True)
print(fruits)

# change value
fruits[0] = 'Blueberries'
print(fruits)