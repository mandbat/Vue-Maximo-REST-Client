import inspect
class MyClass:

    __a1 = "It's a value of Private Attribute"

    def __init__(self, age):
        self.__age = age

    def compareAge(self, obj):
        function_call1 = inspect.stack()[0]
        print (function_call1)
        return self.__age == obj.__age

    def getA(self):
        return self.__a1

    def callPrivateMethod(self, par):
        return self.__privateMethod(par)

    def __privateMethod(self, par):
        return "I'm a private Method called by Public Method with Par = " + str(par)

a = MyClass(23)
b = MyClass(12)
c = MyClass(23)

print ("Age of A is equal B: " + str(a.compareAge(b)))
'''
print ("Age of A is equal C: " + str(a.compareAge(c)))
print (a.getA())
# print (a.__a1)  ERROR
print (a.callPrivateMethod(567))
# print (a.__privateMethod(567)) ERROR
print(a._MyClass__privateMethod(333))
print(dir(a))
'''
function_call = inspect.stack()[0]
print (function_call)
