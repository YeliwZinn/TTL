def pali(n):
    n=str(n)
    return n==n[::-1]

def find():
    n=int(input("Enter a no. :- "))
    try:
        if(pali):
            print(f"{n} is a palindrome")
        else:
            print(f"{n} is not a palindrome.")
    except ValueError:
        print("Invalid input")
        
if __name__=="__main__":
    find()