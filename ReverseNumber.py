n =int(input('enter a number'))
rev = 0

while n > 0:
    
 last= n%10          # Extract the last digit of n
 rev= rev*10 +last  # Add the extracted digit to the reversed number
 n= n//10           # Remove the last digit from n

print('Reverse Number: ', rev)