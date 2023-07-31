def foo(a, b, c):
    if a % 3:
        res = a ** b + c
    elif a % 2:
        res = a * b
    else:
        res = c ** (a + b)
    if a==0:
        print('abc')
    return res

def mp_foo(abc):
    return foo(*abc)