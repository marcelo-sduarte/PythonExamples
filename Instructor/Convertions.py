
"""
File: check04_sample.py
Author: Brother Burton

Purpose: Convert degrees in Fahrenheit to Celsius.
"""

degrees_f = float(input("What is the temperature in Fahrenheit? "))
degrees_c = (degrees_f - 32) * 5 / 9

print(f"The temperature in Celsius is {degrees_c:.1f} degrees.")

# Note: I chose to abbreviate degrees_fahrenheit to degrees_f, because I decided
# that _f and _c were common, known abbreviations, and less likely to introduce
# bugs than if I tried to spell out "fahrenheit" in my code each time. But even
# in that case, I thought "degrees_f" seemed more obvious than the single
# letter variable name of "f".
