class ArithMetic:
    def __init__(self, name, year):
        self._name = name
        self._year = year

    def mult(self,x, y):
        z = x * y
        return z

    def add(self,x, y):
        c = x + y
        return c

#1. constructing an object
#2. Instantiating a class
#3. Initializing a class

arith1 = ArithMetic("Arith1", 2014)
print(arith1._year)









