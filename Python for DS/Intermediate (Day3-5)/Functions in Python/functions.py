def hello_func(greeting):
  return '{} Function.'.format(greeting)

print(hello_func('hi'))

hello_func()
hello_func()
hello_func()
hello_func()
#keeping the code DRY (Don't Repeat Yourself!)

def greet_user():
  #Display a simple greeting
  print("Hello!")
  
greet_user()

def greet_user(username):
  print("Hello, " + username.title() + "!")
  
greet_user("Nithin")

def display_message():
  print("I am learning about functions in this chapter.")
  
display_message()

def favorite_book(title):
  print("One of my favorite book is " +title.title()+ ".")
  
favorite_book("Witcher Series")