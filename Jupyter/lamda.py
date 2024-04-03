def a():
    add = lambda x, y: x / y if y != 0 else "Can't divide"
    
    try:
        a = int(input("Enter a no. :- "))
        b = int(input("Enter another no. :- "))
        r = add(a, b)
        print(f"The division of {a} by {b} is {r}")
    
    except ValueError:
        print("Invalid input")

if __name__ == "__main__":
    a()


