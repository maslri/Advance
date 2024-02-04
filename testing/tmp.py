from random import randint as rnd

def add(x , y) :
    return x + y

def divide(x, y) :
    if y == 0 :
        raise ValueError
    return x / y

def  init_pop(n, m) :
    return [[rnd(0, n-1) for i in range(n)] for i in range(m)]
