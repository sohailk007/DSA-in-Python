# nyc_weather.csv contains new york city weather for first few days in the month of January. Write a program that can answer following,
# What was the average temperature in first week of Jan
# What was the maximum temperature in first 10 days of Jan
# Figure out data structure that is best for this problem

temps = {}

with open("nyc_weather.csv", "r") as file:
    next(file)  # skip the header row
    for line in file:
        day, temp = line.strip().split(',')   # remove newline, split by comma
        temps[day] = int(temp)                # store in dictionary

# 1. Average temperature in first week (Jan 1 – Jan 7)
first_week_days = ["Jan 1", "Jan 2", "Jan 3", "Jan 4", "Jan 5", "Jan 6", "Jan 7"]
first_week_temps = [temps[day] for day in first_week_days]
avg_first_week = sum(first_week_temps) / len(first_week_temps)

# 2. Maximum temperature in first 10 days (Jan 1 – Jan 10)
first_10_days = ["Jan 1","Jan 2","Jan 3","Jan 4","Jan 5","Jan 6","Jan 7","Jan 8","Jan 9","Jan 10"]
first_10_temps = [temps[day] for day in first_10_days]
max_first_10 = max(first_10_temps)

print("Average temperature in first week of Jan:", avg_first_week)
print("Maximum temperature in first 10 days of Jan:", max_first_10)


