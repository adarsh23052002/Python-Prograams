n =int(input('Enter a Number'))
i = 0

while n > 0:
    last = n%10
    i +=1
    n = n//10
        
    
print('Number of Digits: ', i)