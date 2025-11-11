
class computer:

    typ=input('laptop type:')

    def __init__(self):
        self.name=input('enter your name:')
        self.age=int(input('enter your age:'))
        self.ram=input('enter ram size:')


    def show(self):                  #Instance method

        print(f'name:{self.name} age:{self.age}')


    def ram(self):
        print(f'ram:{self.ram}')



    @classmethod                  #Class method
    def lap(cls):
        return print(f'laptop_type:{cls.typ}')



c1=computer()
c1.show()
c1.lap()
computer.ram(c1)


