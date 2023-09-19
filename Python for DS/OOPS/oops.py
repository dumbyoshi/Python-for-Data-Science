#Object Oriented Programming in Python

class Dog:
  def bark(self):
    print("Woof!")

print(type(Dog))


class Robot:
    def introduce_self(self):
        print("Hello , My name is " + self.name)

r1 = Robot()

r1.name = "Tom"
r1.color = "Blue"
r1.weight = 30

r2 = Robot()
r2.name = "Jerry"
r2.color = "Red"
r2.weight = 10

r1.introduce_self()
r2.introduce_self()


class Robot():#class
  def __init__(self, name, color, weight):#constructor
    self.name = name#instance variables
    self.color = color#instance variables
    self.weight = weight#instance variables
    
  def introduce_self(self):#instance method
        print("Hello , My name is " + self.name + ",")#self.name is instance variable
        print("My color is " + self.color + ",")#self.color is instance variable
        print("My weight is " + str(self.weight) + " pounds.")#self.weight is instance variable
        
r1 = Robot("Tom", "Blue", 30)#r1 is object of Robot class
r2 = Robot("Jerry", "Red", 10)#r2 is object of Robot class

r1.introduce_self()#calling method introduce_self() of Robot class