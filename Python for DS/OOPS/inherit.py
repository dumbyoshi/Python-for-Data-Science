class Animal:
  
  alive = True
  
  def Eat(self):
    print("This animal is eating")
  
  def Sleep(self):
    print("This animal is sleeping")
    

class Rabbit(Animal):
    
  def Sleep(self):
    print("This rabbit is sleeping")
    
class Hawk(Animal):
  def Eat(self):
    print("This hawk is eating")
    
    
class Fish(Animal): 
  def Swim(self):
    print("This rabbit is sleeping")
    
rabbit = Rabbit()
hawk = Hawk()
fish = Fish()
 
print(Rabbit.alive)
fish.Swim()
hawk.Eat() 