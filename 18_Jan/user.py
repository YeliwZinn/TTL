def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(d, e):
    return d * e

def div(a, b):
    if b != 0:
        return a / b
    else:
        print("Can't divide")
        return None  
    
def powe(a, b=2):
    return a ** b

def sum_all(*args):
    return sum(args)

a = int(input("Enter a no. :- "))
b = int(input("Enter another no. :- "))

m = add(a, b)
n = sub(a, b)
o = mul(d=a, e=b)
p = div(a, b)
y = powe(a)
x = powe(a, 4)

print(f"The sum of entered numbers is: {sum_all(a, b)}")
print(f"Addition: {m}")
print(f"Subtraction: {n}")
print(f"Multiplication: {o}")
print("Division: ", p)
print(f"Power (Default): {y}")
print(f"Power (Custom): {x}")
