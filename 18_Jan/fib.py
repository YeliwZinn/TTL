def fib(n):
    if n <= 0:
        return "Invalid input. Please enter a positive integer."
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        a, b = 0, 1
        for _ in range(3, n + 1):
            a, b = b, a + b
        return b

def check():
    n = int(input("Enter the value of n to find the nth term of the Fibonacci sequence: "))
    try:
        r = fib(n)
        print(f"The {n}th term of the Fibonacci sequence is: {r}")
    except ValueError:
        print("Invalid input")
        
if __name__=="__main__":
    check()

