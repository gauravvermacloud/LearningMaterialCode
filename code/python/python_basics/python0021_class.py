class my_shape:

    def __init__(self, x, y):
        self._x = x
        self._y = y

    def area(self):
        return self._x * self._y


shape = my_shape(2, 3)
print(shape.area())

################## Duck type ##################


class Duck_Type_Demo_With_Len:

    def __len__(self):
        return 10

    def some_method(self):
        print("Inside Some method")


class Duck_Type_Demo_Without_Len:
    pass


d1 = Duck_Type_Demo_With_Len()
d2 = Duck_Type_Demo_Without_Len()

print(len(d1))

try:
    print(len(d2))
except TypeError:
    print("no len function")

d1.some_method()

try:
    d2.some_method()
except AttributeError:
    print("doesnt have some method")


############### Base Class Example ###############

class My_Base_Class:

    def a_base_method(self):
        print("inside base")

    def override_me(self):
        print("inside base method override me")


class My_Derived_Class(My_Base_Class):

    def method(self):
        print("inside dereived method ")

    def override_me(self):
        print("inside derrive method override me")


my_base_instance = My_Base_Class()

my_base_instance.a_base_method()
my_base_instance.override_me()


my_derived_instance = My_Derived_Class()

my_derived_instance.a_base_method()
my_derived_instance.method()
my_derived_instance.override_me()
