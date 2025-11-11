class computer:

    def __init__(self,cpu,ram):
        self.cpu = cpu
        self.ram = ram


    def config(self):
        print('config is ',self.cpu,self.ram)



com1=computer('i5',16)
com2=computer('i8',32)
print(com1.config())
print(com2.config())
print(com1.cpu)