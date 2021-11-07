
import requests

def add(x, y):
    z = x + y
    m = f'{z}'
    return z


def mult(x, y):
    res = x * y
    return res


mult(4, 0.3)

mult(x=4, y=0.3)

result = mult(y=0.3, x=4)

print(type(result))





