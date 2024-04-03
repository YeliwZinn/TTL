def grade(m):
    if 90 <= m <= 100:
        return 'O'
    elif 80 <= m < 90:
        return 'E'
    elif 70 <= m < 80:
        return 'A'
    elif 60 <= m < 70:
        return 'B'
    elif 50 <= m < 60:
        return 'C'
    elif 40 <= m < 50:
        return 'D'
    elif 0 <= m < 40:
        return 'F'
    else:
        return 'Invalid Input'

def prin():
    try:
        m = float(input("Enter total marks secured: "))
        if 0 <= m <= 100:
            g = grade(m)
            print(f"The grade for {m} marks is: {g}")
        else:
            print("Invalid input. Total marks should be between 0 and 100.")
    except ValueError:
        print("Invalid input. Please enter a valid numeric value.")

if __name__ == "__main__":
    prin()
