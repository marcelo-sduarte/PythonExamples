print()
grade_percentage = float(input('Please insert your grade: '))

if grade_percentage >= 90 :
    letter = 'A'
elif 90 > grade_percentage >= 80 :
    letter = 'B'
elif 80 > grade_percentage >= 70 :
    letter = 'C'
elif 70 > grade_percentage >= 60 :
    letter = 'D'
else:
    letter = 'F'

if grade_percentage >= 70 :
    print(f'Congratulations you pass the course with a letter {letter}')
else:
    print(f'Dont Worry, You can do it better! Your letter grade is {letter}')
