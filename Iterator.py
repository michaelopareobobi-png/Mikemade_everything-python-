class iterate:
    n=int(input('enter number of perfect squares needed between 1 and n:'))

    def __init__(self):
        self.i=1
    def __iter__(self):
        return self
    def __next__(self):
        if self.i<iterate.n:
            d=self.i
            self.i+=1
            return d
        else:
            raise StopIteration



itr=iterate()
m=iterate.n

f=[]
for i in itr:
    f.append(i*i)
    i=i+1
    if f[-1]>m:
        break
del f[-1]
print(f)






