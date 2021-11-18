def func(n):
    return lambda a: a*n
n=2
a=func(n)
for i in range(1,13):
    print(a(i))