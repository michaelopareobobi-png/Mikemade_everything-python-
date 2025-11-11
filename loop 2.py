x=range(0,101)
i=0
while i<101:
    i=i+1
    if i==101:
        break
    if i%3==0:
        continue

    else:
        print(x[i])
