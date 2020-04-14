x=int(input('Enter 1st number'))
y=int(input('Enter 2nd number'))
z=int(input('Enter 3rd number'))

if x>=0:
    print('1st number is Positive')
else:
    print('1st number is Negative')
if y>= 0:
        print('2nd number is Positive')
else:
        print('2nd number is Negative')
if z>=0:
    print('3rd number is Positive')
else:
    print('3rd number is Negative')
if x>y and x>z:
    print('1st number is largest number',x)
elif y>x and y>z:
    print('2nd number is largest number',y)
else:
    print('3rd number is largest number',z)

print('Bye')