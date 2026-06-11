n =int(input('Enter a Number'))
sum = 0

while n > 0: # Write 3 indented statements under while loop

       last=n%10 # Extract the last digit, statement
       sum += last# cumulative Sum update , statement
       n=n//10 # Remove the last digit , statement
    
print('Sum of Digits:', sum)