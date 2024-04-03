def y(a):
    if (a % 4 == 0 and a % 100 != 0) or (a % 400 == 0):
        return True
    else:
        return False

def check():
    try:
        a = int(input("Enter a a: "))
        if y(a):
            print(f"{a} is a leap.")
        else:
            print(f"{a} is not a leap.")
    
    except ValueError:
        print("Invalid input. Please enter a valid a.")

if __name__ == "__main__":
    check()
