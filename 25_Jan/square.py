def a():
    s=lambda a:a*a
    try:
        x=int(input("Enter a no. :- "))
        b=s(x)
        print(f"The square of {x} is {b}")
    except ValueError:
        print("Invalid Input")
        
if __name__=="__main__":
    a()