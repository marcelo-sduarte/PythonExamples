# Import the datatime module so that
# it can be used in this program.
import math
from datetime import datetime
# Call the now() method to get the current date and
# time as a datetime object from the computer's clock.
current_date_and_time = datetime.now()

volume = 0.00

width = int(input("Enter the width of the tire in mm (ex 205): "))
ratio = int(input("Enter the aspect ratio of the tire (ex 60): "))
diameter = int(input("Enter the diameter of the wheel in inches (ex 15): "))
volume = math.pi * width**2 * ratio*(width * ratio + 2540 * diameter) / 10000000
#part_two = width * ratio + 2.540 * diameter
#volume = part_one / 10.000
print(f"The approximate volume is {volume:.1f} milliliters")

# Open a text file named dimensions.txt in append mode.
with open("volumes.txt", "at") as dimens_file:

    # Print a car's model and dimensions to the file.
    print(f"{current_date_and_time.date()}, {width}, {ratio}, {diameter}, {volume}", file=dimens_file)

