import math
class ArithMetic:


    def __init__(self) -> None:
        pass
    def mult(self,x, y):
        z = x * y
        return z

    def add(self,x, y):
        c = x + y
        z = math.floor(c)
        return z

#1. constructing an object
#2. Instantiating a class
#3. Initializing a class
arith1 = ArithMetic()

result = arith1.add(4,5)

arith2 = ArithMetic()
result2 = arith1.add(5,5)




