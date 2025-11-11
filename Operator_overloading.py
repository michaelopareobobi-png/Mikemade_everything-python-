class product:

    def __init__(self,a,b):
        self.a=a
        self.b=b

    def __mul__(self, other):
        a=self.a * other.a
        b=self.b * other.b
        d=product(a,b)
        return d

    def __str__(self):
        return '{} {}'.format(self.a,self.b)



x=product(2,5)
y=product(4,6)
d=x*y
print(d)
