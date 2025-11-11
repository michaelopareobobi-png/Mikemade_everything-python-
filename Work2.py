# Determining the greatest number of three numbers
# Input values
m=int(input("Enter 1st number: "))
n=int(input("Enter 2nd number: "))
o=int(input("Enter 3rd number: "))
if m>n and m>o:
    print('1st number is greater')
elif o>m and o>n:
    print('3rd number is greater')
elif n>m and n>o:
    print('2nd number is greater')


r=int(input('enter number:'))
if r>=0:
    print('positive')
else:
    print('negative')
