#Python's if statement allows us to examine the current state of a program and respond appropriately to that state.
"""if conditional_test:
  do something"""
age = input("Enter your age: ")
if age >=str(18):
  print("You are old enough to vote!")
else:
  print("You are not old enough to vote!")
  
  
#The if-elif-else chain
age = input("Enter your age: ")
if age < str(4):
  print("Your admission cost is $0.")
elif age < str(18):
  print("Your admission cost is $5.")
else:
  print("Your admission cost is $10.")

#we can also use multiple elif blocks as per the needs!.
#we can also omit the else block if it is not needed.


cars = ['jaguar' , 'bmw' , 'audi' , 'masarati' , 'lamborghini']# this is called a list.we can store multiple values in a list.
for car in cars:
  if car == "bmw":
    print(car.upper())
  else :
    print(car.title())
    
  """ 
  Conditional tests
  >>> car = 'bmw'
  >>> car == 'bmw'
  True
  >>> car == 'bmw'
  >>> car == 'audi'
  False
  testing for equality is case sensitive in python.
  numerical comparisons
  >>> age = 18
  >>> age == 18
  True
  These are called conditions and comes in many types.  
  """
users = ['nithin' , 'krish' , 'nithinkrish' , 'nithin krish']
user = 'Mary'
if user not in users:
  print(f"{user.title()}, you can get a response from the forum.")