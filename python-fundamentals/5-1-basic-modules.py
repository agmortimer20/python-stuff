# Simple import statement; Module for working with dates and times
import datetime 

# Import everything from the math module
from math import *

# Only import the randint function from the random module
from random import randint


def get_circle_area(radius):
    return sqrt(pi * radius)

def get_circumference(radius):
    return 2 * pi * radius

# Test out circle functions
radius1 = randint(1, 10)
radius2 = randint(1, 10)
radius3 = randint(1, 10)
area1 = get_circle_area(radius1)
area2 = get_circle_area(radius2)
area3 = get_circle_area(radius3)
circ1 = get_circumference(radius1)
circ2 = get_circumference(radius2)
circ3 = get_circumference(radius3)

print("Function Stuff")
print("--------------")
print(f"Radius {radius1} - Area: {round(area1, 2)}, Circ: {round(circ1, 2)}")
print(f"Radius {radius2} - Area: {round(area2, 2)}, Circ: {round(circ2, 2)}")
print(f"Radius {radius3} - Area: {round(area3, 2)}, Circ: {round(circ3, 2)}")

print("\nDate and Time Stuff")
print("------------")
print(f"Current Date: {datetime.datetime.now().date()}")
print(f"Current Time: {datetime.datetime.now().time()}")