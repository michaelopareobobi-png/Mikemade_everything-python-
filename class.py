
class computer:

    typ='lenovo'

    def __init__(self):
        self.name='navin'
        self.age=28


    def show(self):               #Instance method
        print(self.name,self.age)

    @classmethod                  #Class method
    def lap(cls):
        print('laptop_type {}'.format(cls.typ))

    @staticmethod                 #Static method
    def ram():
        print('ram',8)





c1=computer()
c1.show()
c1.lap()
c1.ram()


