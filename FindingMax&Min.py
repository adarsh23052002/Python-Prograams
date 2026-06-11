numbers = [12, 45, 7, 89, 23]  # You can change these values for testing

n = len(numbers)


i = 0
Max = float('-inf')
Min = float('inf')

#TODO: Write the Logic to chack Max And Min using while loop below
while i<n:
    x=numbers[i]
    i+=1
    if x>Max:
        Max=x
    if x<Min:
        Min=x

print('Max Element:', Max)
print('Min Element:', Min)