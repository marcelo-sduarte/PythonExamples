# Import datetime so that it can be
# used to compute a person's age.
from datetime import datetime


def main():
    # Get the user's gender, birthdate, height, and weight.
    gender = input("Please enter your gender (M or F): ")
    birthday = input("Please enter your birthdate (YYYY-MM-DD): ")
    weigh = float(input("Enter your weight in US pounds: "))
    height = float(input("Enter your height in US inches: "))
    # Call the compute_age, kg_from_lb, cm_from_in, body_mass_index,
    years = compute_age(birthday)
    mass_kg = kg_from_lb(weigh)
    cm_from_inches = cm_from_in(height)
    bmi = body_mass_index (mass_kg,cm_from_inches)

    # and basal_metabolic_rate functions as needed.
    bmr = basal_metabolic_rate(gender, mass_kg,cm_from_inches, years )

    # Print the results for the user to see.
    print(f"Age {years} ")
    print(f"Weight (kg): {round(mass_kg,2)}")
    print(f"Height (inches):{round(cm_from_inches,2)} ")
    print(f"Body mass index: {round(bmi,2)}")
    print(f"Basal metabolic rate (kcal/day):{round(bmr)}")



def compute_age(birth):
    """Compute and return a person's age in years.

    Parameter birth: a person's birthdate stored as
        a string in this format: YYYY-MM-DD
    Return: a person's age in years.
    """
    birthday = datetime.strptime(birth, "%Y-%m-%d")
    today = datetime.now()

    # Compute the difference between today and the birthday in years.
    years = today.year - birthday.year

    # If necessary, subtract one from the difference.
    if birthday.month > today.month or \
        (birthday.month == today.month and birthday.day > today.day):
        years -= 1

    return years


def kg_from_lb(lb):
    """Convert a mass in pounds to kilograms.
    Parameter lb: a mass in US pounds.
    Return: the mass in kilograms.
    """
    mass_kg = lb * 0.45359237 
    return mass_kg


def cm_from_in(inch):
    """Convert a length in inches to centimeters.
    Parameter inch: a length in inches.
    Return: the length in centimeters.
    """
    cm_from_inches = inch * 2.54 
    return cm_from_inches


def body_mass_index(weight, height):
    """Calculate and return a person's body mass index (bmi).
    Parameters:
        weight must be in kilograms.
        height must be in centimeters.
    Return: a person's body mass index.
    """
    bmi = (10000 * weight) / (height**2)
    return bmi


def basal_metabolic_rate(gender, weight, height, age):
    """Calculate and return a person's basal metabolic rate (bmr).
    Parameters:
        weight must be in kilograms.
        height must be in centimeters.
        age must be in years.
    Return: a person's basal metabolic rate in kcal per day.
    """
    if gender == "F":
        bmr = 447.593 + 9.247 * weight + 3.098 *height - 4.330 * age
    elif gender == "M":
        bmr = 88.362 + 13.397 * weight + 4.799 * height - 5.677 * age
    return bmr

main()

# Call the main function so that
# this program will start executing.