numbers = []
number= ""
result = 0
count = -1
largest_number =0
average = 0

print("Enter a list of numbers, type 0 when finished.")
while number != 0:
    number = float(input("Enter a number."))
    numbers.append(number)
    
for index_number in numbers:
    result += index_number
    count= count + 1

average = result / count

for index_number in numbers:
    if index_number > largest_number:
        largest_number = index_number


print(f"The sum is: {result:.2f}")
print(f"The average is: {average:.2f}")
print(f"The largest number is: {largest_number:.2f}")
