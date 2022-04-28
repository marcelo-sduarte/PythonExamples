"""
File: teach08_stretch_sample.py
Author: Brother Burton

Purpose: Demonstrates using loops within loops.
"""
# This will be used to compute the number of digits later
import math

user_choice = int(input("How many columns and rows do you want in your multiplication table? "))

# Determine the maximum number in the table:
max_number = user_choice * user_choice

# Approach 1: Using an if statement
# digits = 2
# if max_number >= 100:
#     digits = 3

# Approach 2: Computing the digits in math
# To find the number of digits, we want to know what power of 10 is this number (there is a
# mathematical operation to compute this called a logarithm).
# math.log10(25) is: 1.398
# math.log10(99) is: 1.996
# math.log10(100) is: 2.000

# Then, by converting it to an integer, it will drop the decimal part.
# Finally, we can then add 1 and we have the number of digits!

digits = int(math.log10(max_number)) + 1

# When we use range() in the loop below, it will go up to, but NOT INCLUDING the number
# so here we set the range_size to be the user's choice plus one.
range_size = user_choice + 1

# Iterate through that number of rows
for row_number in range(1, range_size):
    # For each for, we will also iterate through the same number of columns
    for col_number in range(1, range_size):
        # The number to display is the product of the row_number and the col_number
        number = row_number * col_number

        # Display the number with a space instead of a newline at the end: `end=" "`

        # This is a little tricky. If we just need the number 3, we could right:
        # print(f"{number:3}", end=" ")
        # But, since it is a variable number of digits, we have to put the variable name `digits`
        # inside of {}'s as well: {digits}
        print(f"{number:{digits}}", end=" ")
    
    # We have now printed all of the columns and are done with the row.
    # So it is now time to start a new line.
    print()