def prime(b):
    if b < 2:
        return False
    for i in range(2, int(b**0.5) + 1):
        if b % i == 0:
            return False
    return True

def check_prime():
    try:
        b = int(input("Enter a number: "))
        if prime(b):
            print(f"{b} is a prime number.")
        else:
            print(f"{b} is not a prime number.")

    except ValueError:
        print("Invalid input")

if __name__ == "__main__":
    check_prime()
