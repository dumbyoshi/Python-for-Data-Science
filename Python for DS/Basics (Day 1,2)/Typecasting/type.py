#Explicit typecasting: converting one data type to another data type manually:
name ='Nithin'
age = 21
grade = 2.4
student = True

type(name)
print(type(name))
print(type(age))
print(type(grade))
print(type(student))

age = float(age)
print(age)

gpa = int(grade)
print(gpa)

student = str(student)
print(student)

age = bool(age)
print(age)#empty strings are false and non empty strings are true.

#Implicit typecasting: converting one data type to another data type automatically:
x = 2
y = 4.5 
print(x*y)
print(type(x*y))