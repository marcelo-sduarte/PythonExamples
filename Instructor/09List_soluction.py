
"""
File: teach09_sample.py
Author: Brother Burton

Purpose: Practice using numbers in lists.
"""

# Please note: For this program especially, there are MANY ways to accomplish the task.
# The following shows one way it can be done, but it's not the only way. In particular, many
# of these tasks can be done with built-in functions (such as max(numbers)), but this
# approach highlights how to compute those values directly using loops.

print("Enter a list of numbers, type 0 when finished.")

numbers = []
number = -1

while number != 0:
    number = int(input("Enter number: "))

    if number != 0:
        numbers.append(number)

# The list "numbers" now has all the numbers the user typed

# Step 1: Find the sum or total
sum = 0

for number in numbers:
    sum += number

print(f"The sum is: {sum}")

# Step 2: Find the average
# We can use the sum we just computed...
count = len(numbers)
average = sum / count

print(f"The average is: {average}")

# Step 3: Find the max
# We will walk through the numbers again, this time keeping track
# of the best so far, or the highest number to that point.

best_so_far = -1

for number in numbers:
    # Check if this number is larger than the best one we have seen so far
    if number > best_so_far:
        # This is the new best number, so save it to that variable
        best_so_far = number


print(f"The largest number is: {best_so_far}")


########################
# Stretch Challenges
########################

# Stretch Challenge 1: Find the smallest positive number:

# We need to start with something large
smallest_so_far = 99999999999

# Note: If we wanted to be the most accurate here, instead of starting with a big
# number like above, we should loop through the list until we find a positive number
# and use that as the smallest_so_far. I'm going with the approach here, because it's
# simpler to see and understand, but what if the list didn't have any positive numbers?
# What if it didn't have any less than the big number I picked? These would create
# problems that would be solved by the approach mentioned.

for number in numbers:
    if number > 0 and number < smallest_so_far:
        # We have a new smallest number
        smallest_so_far = number

print(f"The smallest positive number is: {smallest_so_far}")

# Stretch Challenge 2: Sorting the list
sorted_list = sorted(numbers)

print("The sorted list is:")
for number in sorted_list:
    print(number)
