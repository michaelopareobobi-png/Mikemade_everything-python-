def fib(m):
    x=[0,0,1]
    x[1]=0
    x[2]=1
    m=int(input("enter number of sequence needed(from '1' to 'nth'):"))
    if m==1:
        print(x[1])
    if m==2:
        print(x[1:])
    if m <=0:
        print('Invalid input...')
        print('Input should start from "1"')

    i=3
    while i>=3:
        y=x[i-1]+x[i-2]
        x.append(y)
        i=i+1
        if len(x)==m:
            break
    x.pop(0)
    return x
result=fib(50)
print(result)
