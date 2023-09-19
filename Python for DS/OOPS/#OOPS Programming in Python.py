#OOPS  in Python

class Robot():
  def __init__(self, name, color, weight):
    self.name = name
    self.color = color
    self.weight = weight
    
  def introduce_self(self):
        print("Hello , My name is " + self.name + ",")
        print("My color is " + self.color + ",")
        print("My weight is " + str(self.weight) + " pounds.")
        
r1 = Robot("Tom", "Blue", 30)
r2 = Robot("Jerry", "Red", 10)

r1.introduce_self()