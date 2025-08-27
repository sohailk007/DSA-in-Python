# nyc_weather.csv contains new york city weather for first few days in the month of January. Write a program that can answer following,
# What was the temperature on Jan 9?
# What was the temperature on Jan 4?
# Figure out data structure that is best for this problem

temps = {}

with open("nyc_weather.csv","r") as file:
    next(file)
    for line in file:
        day, temp = line.strip().split(',')
        temps[day] = int(temp)
        
print(f"January 9 Temperature is {temps["Jan 9"]}")
print(f"January 4 Temperature is {temps["Jan 4"]}")
        
        