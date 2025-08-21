# Find the square root time complexity more elements in array takes more time

def get_squared_number(numbers):
    
    squared_numbers = []
    
    for n in numbers:
        squared_numbers.append(n*n)
        
    return squared_numbers

number=[1,2,3,4,5,6,7]

sq_result= get_squared_number(number)

print(sq_result)

################################################

def user_square_number():
    
    numbers = int(input("Enter the number :" ))
    
    square_number = numbers*numbers
    
    return square_number

k = user_square_number()

print(k)

#####################################################

# Find the duplicate value

numbers = [3,6,2,4,3,6,8,9]

for i in range(len(numbers)):
    for j in range(i+1, len(numbers)):
        if numbers[i] == numbers[j]:
            print(numbers[i])
            break
        
############################################

# Find the specific number

num = [4,5,4,2,66,7,77,88,90]

for i in range(len(num)):
    if num[i] == 66:
        print(i)
    
    
    




