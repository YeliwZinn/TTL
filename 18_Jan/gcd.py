def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def find():
    n = int(input("Enter the first number: "))
    m = int(input("Enter the second number: "))

    r = gcd(n, m)
    print(f"The GCD of {n} and {m} is: {r}")

if __name__=="__main__":
    find()