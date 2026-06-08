amount=float(input('Enter your bill amount:'))

if(amount<1000):
    total= amount-amount*10/100
elif(amount>=1000 and amount<5000):
   total= amount-amount*15/100
elif(amount>=5000 and amount<10000):
   total= amount-amount*20/100
else:
   total= amount-amount*25/100


print('Your discounter bill is :',total)         