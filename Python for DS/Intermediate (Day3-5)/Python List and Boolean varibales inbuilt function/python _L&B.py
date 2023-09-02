#Python list and boolean Variables Inbuilt functions:
#LIST:
#append() - Adds an element at the end of the list
cars = ['Ford', 'BMW', 'Volvo']
cars.append("Honda")
print(cars)

#insert() - Adds an element at the specified position
cars.insert(1, "Toyota")
print(cars)

#Extend:
num = [1,2,3,4,5]
num.extend(cars)
print(num)

#sum() - Returns the sum of all elements in the list
num = [6,5,6,2,1]
print(sum(num))

#pop() - Removes the element at the specified position
num.pop(2)
print(num)

#count() - Returns the number of elements with the specified value
print(num.count(6))

#index() - Returns the index of the first element with the specified value
#max() - Returns the value of the largest element in the list
#min() - Returns the value of the smallest element in the list

#----------------------------------------------------------------------------------------------------------------------------

#Boolean Variable Inbuilt functions:
my_name = 'Nithin'
print(my_name.isalnum())
#isalnum() - Returns True if all characters in the string are alphanumeric
print(my_name.isalpha())
#isalpha() - Returns True if all characters in the string are in the alphabet
print(my_name.isascii())
#isascii() - Returns True if all characters in the string are ascii characters
print(my_name.isdecimal())
#isdecimal() - Returns True if all characters in the string are decimals
print(my_name.isdigit())
#isdigit() - Returns True if all characters in the string are digits
print(my_name.isidentifier())
#isidentifier() - Returns True if the string is an identifier
print(my_name.islower())
#islower() - Returns True if all characters in the string are lower case
print(my_name.isnumeric())
#isnumeric() - Returns True if all characters in the string are numeric
print(my_name.isprintable())
#isprintable() - Returns True if all characters in the string are printable
print(my_name.isspace())
#isspace() - Returns True if all characters in the string are whitespaces



