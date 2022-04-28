"""

06 Teach: Team Activity
Amusement Park Rides

"""
can_ride = False

age_first_rider = int(input('How old is the first rider? '))
height_first_rider = float(input('What is the height of the first rider? '))

second_rider = input('Is there a second rider (yes/no)? ')

if second_rider.lower() == 'yes' :
    age_second_rider = int(input('How old is the second rider? '))
    height_second_rider = float(input('What is the height of the second rider? '))

    if height_first_rider >= 36 and height_second_rider >= 36 :
        if age_first_rider >= 18 or age_second_rider >= 18 :
            can_ride = True

else:
    if height_first_rider >= 36 :
        if age_first_rider >= 18 and height_first_rider >= 62 :
            can_ride = True

if can_ride :
    print('Welcome to the ride. Please be safe and have fun!')

else:
    print('Sorry, you may not ride. Go to the carousel')