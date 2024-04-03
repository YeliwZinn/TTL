def oe():
    try:
        a = int(input("Enter a a:- "))
        if a % 2 == 0:
            print(f"{a} is an even.")
        else:
            print(f"{a} is an odd.")
    
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    oe()