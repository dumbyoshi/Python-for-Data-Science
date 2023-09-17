#also called as anonymous function, works like a normal function but without a name , works faster and easy to use.
def addition(a,b):
    return a+b
  
addition(2,3)

addition = lambda a,b: a+b
addition(2,3)

def even (a):
  if a%2 == 0:
     return True
   
even(6)

even = lambda a : a%2==0
even(24)

addition = lambda a,b,c : (a+b+c)
addition(2,4,5)