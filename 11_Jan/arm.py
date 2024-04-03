def arm(b):
    
    x = str(b)
    num_digits = len(x)
    
    armstrong_sum = sum(int(digit) ** num_digits for digit in x)
    return armstrong_sum == b

if __name__ == "__main__":
    try:
        
        b = int(input("Enter a no to check if it's an Armstrong :- "))

       
        if arm(b):
            print(f"{b} is an Armstrong.")
        else:
            print(f"{b} is not an Armstrong.")

    except ValueError:
        print("Invalid input. Please enter a valid a.")
