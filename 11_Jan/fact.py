import math
def fac():
    a=int(input("Enter a no. :-"))
    try:
        b=math.factorial(a)
        print(f"The factorial of {a} is {b}")
    except ValueError:
        print("Invalid input")

        
if __name__=="__main__":
    fac()