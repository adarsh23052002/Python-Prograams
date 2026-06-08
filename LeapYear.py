year=int(input('Enter a Year :'))


if(year%100==0):
    if(year%400==0):
      print('Its a Leap year 1')
    else:
        print('not a leap year')  
        
elif (year%4==0):
    print('Its a Leap year')
else:
    print('Its not a Leap Year')

  