from functools import reduce

x=[]
for i in range(1,11):
    x.append(i)
odds=list(filter(lambda n:n%2!=0,x))     #tuple also works perfectly
trip=list(map(lambda x:x*3,odds))
pro=reduce(lambda x,y:x*y,trip)

print(odds)
print(trip)
print(pro)