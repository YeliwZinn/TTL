n = [1, 2, 3, 4, 5, 6, 7]
for a in filter(lambda a: a%2 ==0,n):
    n.append(a)
print(a)
# t = list(map(lambda x: x % 2==0, n))
# print("Even:", t)

# w = ['apple', 'banana', 'pie']
# u = sorted(w, key=lambda x: len(x))
# print(u)

