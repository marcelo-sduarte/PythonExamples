
import math

items = int(input("Enter the number of items: "))
box = int(input("Enter the number of items per box: "))

result = items / box



print(f"For {items} items, packing {box} items in each box, you will need {math.ceil(result)} boxes.")