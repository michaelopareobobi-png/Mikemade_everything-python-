# Duck-typing from Polymorphism involves multiple number of classes.
# provided that all number of classes have same method(function) name under it(ie:'IDE'),
# then, a counter class can be created with its method(function) having two arguments(self & 'A'),
# where the que of that class can be made to execute the output from the other classes by using the expression;
# "A.IDE()"....  To do this you must first create the object for that counter class;
# then relate "IDE"(argument variable from the counter class) to the class of interest??
# ie: IDE=l()..... ,where "l" is the class name....

class A:
    def tap(self):            # tap.... common method name
        print('today...')

class B:
    def tap(self):            # tap..... common method name
        print('yesterday...')

class C:
    def hat(self,idle):       # new argument variable(idle) in method of counter class
        idle.tap()            # executionable expression??(linked to common method name(tap) from each class)


idle=A()                      # linkage of new argument variable to class of interest
f=C()                         # object of counter class
f.hat(idle)                   # output of executionable expression
