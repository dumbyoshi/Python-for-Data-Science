#Variables
message = "Hello World !"#Variables are used to store values,here message is a variable which stores the value "Hello World !"
print(message) #print() is a function used to print the value of the variable message.
#Variables can be names as message_1 , but not 1_message

#Strings
"this is a string"
'this is aslo a string' 
#here we can use two types of quotes to define a string.
'Hy , i am "Nithin"'#here we can use double quotes inside single quotes.

#Changing case in a string with methods
name = 'nithin krish'
print(name.title())#title() is a method used to change the first letter of each word to uppercase.
print(name.upper())#upper() is a method used to change the whole string to uppercase.
print(name.lower())#lower() is a method used to change the whole string to lowercase.

first_name = "Nithin"
last_name = "Krish"
full_name = f"{first_name} {last_name}" #f is format , f-strings are used to combine strings and variables.
print(full_name)
print(f"Hello , {full_name.title()} !")

print(len("Nithin"))#len() is used to find the length of the string.

print("what's ur name?")
name = input()#input() is used to take input from the user.
print(f"Hello , {name.title()} !")

#checking data type!
print(type("Nithin"))#str
print(type(1))#int
print(type(1.1))#float
print(type(True))#boolean

#to add a tab to your text use \t
#>>>print("\tHello")
#to add a new line to your text use \n
#>>>print("Hello\nWorld")
#.rstrip() is used to remove the white spaces at the end of the string.
#.lstrip() is used to remove the white spaces at the beginning of the string.
#to remove prefix and suffix spaces use .strip() also .removeprefix() and .removesuffix() can be used.

#Syntax Errors
#print("Hello World"s")



