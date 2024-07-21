# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
 
#Create Tuple
fruits = ('Apples', 'Oranges', 'Grapes')

print(fruits, type(fruits))

print(fruits[1])

# can't change it
# fruits[0] = 'Pears'

#Get length
len(fruits)

# A Set is a collection which is unordered and unindexed. No duplicate members.

#Create Set
fruits_set = {'Apples', 'Oranges', 'Mango'}
print(fruits_set, type(fruits_set))

#check if in set
print('Apples' in fruits_set)

# add to set
fruits_set.add('Grape')
print(fruits_set)

#clear set
# fruits_set.clear()
# print(fruits_set)
