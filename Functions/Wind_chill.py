"""
By Marcelo Duarte
"""
# Function to convert temperature from Celsius to Fahreinheit
def convert_temperature (degree):
    return (degree * 9/5) + 32

# Function to convert temperature and speed to wind chill
def convert_wind_chill (temp,speed):
    return 35.74+(0.6215*temp)-(35.75*(speed**0.16))+((0.4275*temp)*(speed**0.16))

# Declare list to MPH        
velocitys = [5,10,15,20,25,30,35,40,45,50,55,60]

# input to insert values
answer_one = float(input("What is temperature?"))
answer_two = input("Fahrenheit or Celsius (F/C)?")

if answer_two == "C":
    result = convert_temperature(answer_one)  
else:
    result = answer_one

for i in range(len(velocitys)):
    wind_chill = convert_wind_chill(result,velocitys[i])
    print(f"At temperature {result:.2F}F, and wind speed {velocitys[i]}mph, the windchill is: {wind_chill:.2F}F")