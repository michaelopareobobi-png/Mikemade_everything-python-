l=[2,5,7,8,9,6,4,1,2,5,8,6,3,9]
l.sort()
s=l[-1]
for i in range(len(l)-2,-1,-1):
    if l[i]==s:
        del l[i]
    else:
        s=l[i]

print(l)
