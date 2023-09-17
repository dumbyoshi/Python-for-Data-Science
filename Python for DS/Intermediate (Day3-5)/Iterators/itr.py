#Interators 
# An iterator is an object that contains a countable number of values.
lst = [1,2,3,4]
for i in lst:
  print(i)

#iterator
iterable = iter(lst)
for i in iterable:
  print(i)
else:
  print("End of list")
  
try:
  print(next(iterable))
except StopIteration:
  print("The list is empty")
