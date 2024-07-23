# Python has functions for creating, reading, updating, and deleting files.

myFile = open('myfile.txt', 'w')

print('Name: ', myFile.name)
print('Is Closed : ', myFile.closed)
print('Opening Mode: ', myFile.mode)

#Write

myFile.write('I love Python')
myFile.write(' bt not Javascript')
myFile.close

# Append
myFile = open('myfile.txt', 'a')
myFile.write(' but do PhP')
myFile.close

# read from file
myFile = open('myfile.txt', 'r+')
text = myFile.read(50)
print(text)