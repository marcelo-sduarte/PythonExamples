import math

temperature_fahrenheidt = float(input("What is the temperature in Fahrenheidt? "))
result = temperature_fahrenheidt - 32
result = (result * 0.5555555555555556)
result = round(result,2)
print(f"The temperature in Celsius is {result} degrees.")