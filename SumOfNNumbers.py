numbers = [2, 5, 9, 6, 4] 

n = len(numbers)    
i = 0
Sum = 0

#TODO Write the logic to compute Sum of numbers using while loop below
while i<n:
    x=numbers[i]
    Sum += x
    i= i+1
    
print(Sum)