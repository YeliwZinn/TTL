def calex(a, b, c, d, x, cube, sq):
    y = a * cube(x) + b * sq(x) + c * x + d
    return y


x = 5
a = 2
b = 3
c = 2
d = 1

cube = lambda x: x * x * x
sq = lambda x: x * x

result = calex(a, b, c, d, x, cube, sq)
print(result)