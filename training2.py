class ArithMetic:
    
    def __init__(self, name):
        self._myName = name
        
    def add(self,x, y):
        z = x + y
        m = f'{z}'
        return z


    def mult(self,x, y):
        res = x * y
        return res



arm1 = ArithMetic(name="aaron")

print(arm1._myName)

result = arm1.add(4, 5)

result2 = arm1.mult(3, 0.3)


