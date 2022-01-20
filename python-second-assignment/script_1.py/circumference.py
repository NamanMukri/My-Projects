import math
def take_input():
  return int(input("Enter Radius: "))
radius=take_input()
def circumference(radius):
  return (2*math.pi*radius)
circumference=circumference(radius)
print(circumference)

