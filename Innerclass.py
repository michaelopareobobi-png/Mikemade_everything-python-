class school:

    def __init__(self,name,age):
        self.name=name
        self.age=age
        self.inf=self.info('h1','Science')

    def student(self):
        print(self.name,self.age)
        self.inf.student()


    class info:

        def __init__(self,house,course):
            self.house=house
            self.course=course

        def student(self):
            print(self.house,self.course)



s1=school('kofi',15)
s1.student()
