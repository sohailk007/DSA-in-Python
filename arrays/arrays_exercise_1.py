# Exercise 1: Array DataStructure
# Let us say your expense for every month are listed below,
# January - 2200
# February - 2350
# March - 2600
# April - 2130
# May - 2190
# Create a list to store these monthly expenses and using that find out,

# 1. In Feb, how many dollars you spent extra compare to January?
# 2. Find out your total expense in first quarter (first three months) of the year.
# 3. Find out if you spent exactly 2000 dollars in any month
# 4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
# 5. You returned an item that you bought in a month of April and
# got a refund of 200$. Make a correction to your monthly expense list
# based on this

# Create list of monthly expenses
monthly_expenses = [2200, 2350, 2600, 2130, 2190]
print("Initial monthly expenses:", monthly_expenses)
print("-" * 67)

# 1. Extra dollars in February compared to January
feb_extra = monthly_expenses[1] - monthly_expenses[0]
print(f"1. Extra dollars spent in February compared to January: ${feb_extra}")

# 2. Total expense in first quarter (Jan, Feb, Mar)
first_quarter_total = monthly_expenses[0] + monthly_expenses[1] + monthly_expenses[2]
print(f"2. Total expense in first quarter: ${first_quarter_total}")

# 3. Check if spent exactly $2000 in any month
spent_2000 = 2000 in monthly_expenses
print(f"3. Spent exactly $2000 in any month: {spent_2000}")

# 4. Add June expense
monthly_expenses.append(1980)
print(f"4. Added June expense: ${monthly_expenses[-1]}")
print("   Expenses after adding June:", monthly_expenses)

# 5. April refund correction
monthly_expenses[3] -= 200
print(f"5. Updated April expense after refund: ${monthly_expenses[3]}")
print("   Final expenses:", monthly_expenses)

