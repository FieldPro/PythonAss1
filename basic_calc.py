import math

print("Basic Calculator for Area of a Circle")
print("_____________________________________________")
p = math.pi
r = float(input("Insert the radius: "))
print("_____________________________________________")
def calc(p, r):
  return p * r
a = p * r ** 2
print("The area of the circle is: " + str(a))