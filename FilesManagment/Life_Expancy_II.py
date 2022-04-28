min = 200.000
max = -1
min_overall = 200.000
max_overall = -1
sum = 0
total = 0
average= 0
count=0
lives_average = []
years_country = []
cities = []

year_interest = int(input("Enter the year of interest:"))

with open ("life-expectancy.csv") as newfile:
    #1 Recovery date 
    for file in newfile:
        file = file.strip() # remove espaço entre linhas
        parts = file.split(",") # separa em virgula
        years = (parts[2])
        if years != "Year":
            life_expectativs = float(parts[3])
            lives_average.append(life_expectativs)
            countrys = parts[0]
            cities.append(countrys)
            years_int = int(parts[2])
            years_country.append(years_int)
            if life_expectativs > 0 and life_expectativs < min_overall:
                min_overall = life_expectativs 
                min_overall_city = countrys
                min_overall_year = years_int
                
            if life_expectativs < 200.00 and life_expectativs > max_overall:
                max_overall = life_expectativs
                max_overall_city = countrys
                max_year = years_int
    print()
    print(f"The overall max life expectancy is: {max_overall} from {max_overall_city} in {max_year}")
    print(f"The overall min life expectancy is: {min_overall} from {min_overall_city} in {min_overall_year}")
    print() 

    for i in range(len(lives_average)):
        if year_interest == years_country[i]:
            average = lives_average[i]
            sum += average
            count= count + 1
            city = cities[i]
            if average > 0 and average < min:
                min = average
                min_city = city
            if average < 200.00 and average > max:
                max = average
                max_city = city
    
print(f"For the year {year_interest}:")
if average == 0 :
    print (f"The year {year_interest} don't founded!\
            \n Please try another year before {year_interest}... ")
else:
    average = sum / count   
    print(f"The average life expectancy across all countries was {average:.2f}")    
    print(f"The max life expectancy was in {max_city} with {max}")
    print(f"The min life expectancy was in {min_city} with {min}")