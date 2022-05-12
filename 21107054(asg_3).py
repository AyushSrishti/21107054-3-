
# Q1

# input number 
number = int(input("Enter a number :"))

# converting to binary and printing 
print("The binary of the number is :",((bin(number).replace('0b',''))))

#Q2

# input numbers and operators
num_1 = float(input("first number :"))
operator = input("Available operators:\n For Addition:(+)\n For Subtraction:(-)\n For Multiplication:(*)\n For Division:(/)\n For Floor Division:(//)\n For Modulus:(%)\n Enter the operator to be used:")
num_2 = float(input("enter second number :"))

# Printing results for various operators

if operator =="+":
  print("Result :",num_1+num_2)
elif operator =="-":
  print("Result :",num_1-num_2)
elif operator == "*":
  print("Result :",num_1*num_2)
elif operator == "/":
  print("Result :",num_1/num_2)
elif operator == "//":
  print("Result :",num_1//num_2)
elif operator == "%":
  print("Result :",num_1%num_2)
else:
  print("Error ! use a correct operator and try again...")

# Q3
from math import pi
from math import sin
from math import cos
# Equation 1
print('(3 + 4) * 5')
print('Result:', (3 + 4) * 5)
# Equation 2
print('n*(n-1)/2')
n = int(input('Enter the value of n:'))
print('Result:', n*(n-1)/2)
# Equation 3
print('4 * pi * r**2')
r = float(input('Enter the value of radius:'))
print('Result:', 4 * pi * r**2)
# Equation 4
print('r * cos(a)**2 + r * sin(b)**2) ** 0.5')
a = float(input('Enter the angle of sin:'))
b = float(input('Enter the angle of cos'))
print('Result:', (r * cos(a)**2 + r * sin(b)**2) ** 0.5)
# Equation 5
print('(y2 - y1) / (x2 - x1)')
y2 = float(input('Enter the value of y2:'))
y1 = float(input('Enter the value of y1:'))
x2 = float(input('Enter the value of x2:'))
x1 = float(input('Enter the value of x1:'))
print('Result:', (y2 - y1) / (x2 - x1))

#Q4

# initializing
result = "a. "
# assigning range
x = range (5) 
for n in x:
 result += str(n)+", "
print(result)

result ="b. "
x = range(3,10)
for n in x:
  result +=str(n) + ", "
print(result)

result = "c. "
x = range(4, 13, 3)
for n in x:
  result += str(n) + ", "
print(result)

result = "d. "
x = range(15, 5, -2)
for n in x: 
 result +=str(n) +", "
print(result)

result = "e. "
x = range(5,3)
for n in x:
  result += str(n) + ", "
print(result)

# Q5
# Given weights of individual atoms
weight_of_hydrogen = 1.00794
weight_of_carbon = 12.0107
weight_of_oxygen = 15.9994

# Entering the number of atoms in the molecule
no_of_hydrogen = int(input("Enter the number of hydrogen atoms in the carbohydrate molecule:"))
no_of_carbon = int(input("Enter the number of carbon atoms in the carbohydrate molecule:"))
no_of_oxygen = int(input("Enter the number of oxygen atoms in the carbohydrate molecule:"))

# Calculating the weight of carbohydrate
weight_of_carbohydrate = no_of_carbon*weight_of_carbon + no_of_oxygen*weight_of_oxygen + no_of_hydrogen*weight_of_hydrogen

# Printing the answer
print(weight_of_carbohydrate)
