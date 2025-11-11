# Printing of numbers from 1 to 100, ignoring numbers divisible by 3 or 5
x=range(1,101)
for i in x:
    if i%3!=0 and i%5!=0:
        print(i)


