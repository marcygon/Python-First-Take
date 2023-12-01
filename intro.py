#Inline comment

print('Hello World')

#Variable in lowercase and constant in uppercase. Snake_case in variables.
PI = 3.14
name = 'Marcy'
is_cool = True

#How to transform a string to a number
string_num = '1'
num = int(string_num)
result = 'Hi player ' + num
print(type(num))#class 'int'

#abs() returns the absolute value of a number
num = -10
absolute = abs(num)
print(absolute) #10

#Round() rounds the number to the nearest integer or to a specific number of decimals
num = 3.7
rounded = round(num)
print(rounded) #4

num = 3.14159
rounded_2_decimals = round(num, 2)
print(rounded_2_decimals) #3.14

#min() returns the minimum value of a series of numbers or elements
numbers = [5, 2, 8, 1, 10]
minimum = min(numbers)
print(minimum) #1

#max() returns the maximum value of a series of numbers or elements
maximum = max(numbers)
print(maximum) #10

#sum() calculates the sum of a series of numbers
numbers_sum = [1, 2, 3, 4, 5]
sum_num = sum(numbers_sum) #10

#Strings
char = name[1] #Access to individual characters
lenght = len(name)#Length of a string
mayus = name.upper #String in uppercase
minus = name.lower() #String in lowercase
message = 'I\m a old message'
replace = message.replace('old message', 'new message') #Replace the selected part

#Lists
fruits = ['Apple', 'Banana', 'Pear']
fruits[2] = 'Kiwi' #Apple, Kiwi, Pear
fruits.append('Orange') #Apple, Kiwi, Pear, Orange
last_fruit = fruits.pop()

print(last_fruit) #Orange
print(fruits) # Apple, Kiwi, Pear

for fruit in fruits:
		print(fruit) #Print each element of the list on a separate line

fruits.remove('Pear')

#Dicctionary
person = { 
		'name': 'Jane', 
		'age': 30, 
		'city': 'London'
}

#Accessing values using keys
print(person['name']) #Jane
print(person['age']) #30

#Modification of values
person['age'] = 40

#Adding new key-value pairs
person['occupation'] = 'Developer'

#Delete key-value pair
del person['city']

#Get a list of keys or values from a dictionary
keys = list(person.keys())
values = list(person.values())

fruits = {'Apple', 'Orange', 'Pear'} #Set declaration
empty_set = set() #Empty set creation
fruits.add('Mango') #Add elements to the set
fruits.remove('Orange') #Delete elements from the set

#Union of sets
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union = set1.union(set2)
print(union) #1, 2, 3, 4, 5

#Intersection of sets
intersection = set1.intersection(set2)
print(intersection) #3

#For loop
for fruit in fruits:
	print(fruit)

#While loop
count = 0
while count < 5:
	print(count)
	count += 1

#Scope
global_variable = 20

def another_function():
    print(global_variable)

another_function()#20

def modify_variable():
    global global_variable
    global_variable = 40

modify_variable()#40