years= []
countrys = []
life_expectativs = [] 
min_overall = "200.000"
max_overall = ""
sum = 0
total = 0
average=""
count=""

year_interest = input("Enter the year of interest:")

with open ("life-expectancy.csv") as newfile:
    #1 Recovery date 
    for file in newfile:
        file = file.strip() # remove espaço entre linhas
        file = file.split(",") # separa em virgula
        years.append(file[2])
        life_expectativs.append(file[3])
        countrys.append(file[0])

    for i in range(len(years)) :
        if i != "Year":
            if life_expectativs[i] > "0" and life_expectativs[i]  < min_overall:
                min_overall = life_expectativs[i] 
                min_city = countrys[i]
                min_year = years[i]
    
    for j in range(len(years)) :
        if i != "Year":
            if life_expectativs[j] < "200.00" and life_expectativs[j] > max_overall:
                max_overall = life_expectativs[j] 
                max_city = countrys[j]
                max_year = years[j]
    print()
    print(f"The overall max life expectancy is: {max_overall} from {max_city} in {max_year}")
    print(f"The overall min life expectancy is: {min_overall} from {min_city} in {min_year}")
    print() 
    print(f"For the year {year_interest}:")
      
    for z in range(len(years)):
        if year_interest == years[z]:
         total = life_expectativs[z]
         sum = sum + total
    count=len(life_expectativs)   
    average = sum / count
    print(f"The average life expectancy across all countries was {average:.2f}")
    
'''print(f"The max life expectancy was in {} with {}")
    print(f"The max life expectancy was in {} with {}")
'''