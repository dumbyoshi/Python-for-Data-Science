#diff between iterator and Generator
#to create a iterator we use iter() and for generator we define a fucntion and use yield keyword

def square(n):
  for i in range(n):
    yield i**2
    
for i in square(3):
  print(i)

# https://youtu.be/rDj8EBv9ErA