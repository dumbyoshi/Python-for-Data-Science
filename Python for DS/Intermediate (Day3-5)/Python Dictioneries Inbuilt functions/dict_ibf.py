#dictionaries 
#A dictionary is a collection which is unordered, changeable and indexed. In Python dictionaries are written with curly brackets, and they have keys and values.
dict = {}
car_dict = {"brand 1" : "BMW" , "brand 2" : "Audi" , "brand 3" : "Mercedes" , "brand 4" : "Volkswagen"}
print(car_dict["brand 1"])
type(car_dict)

for x in dict:
  print(x)
  
for x in car_dict.values():
  print(x)
  
for x in car_dict.items():
  print(x)  
  
car_dict["brand 5"] = "Ferrari"

#Nested Dictionaries:
car1_model = {"BMW" : 1960}
car2_model = {"Ferrari" : 1980}
car_type = {"car1" : car1_model , "car2" : car2_model}
print(car_type["car1"])
