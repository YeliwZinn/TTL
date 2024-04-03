def sum():
    b=int(input("Enter a no. :- "))
    try:
        n=0
        a=b
        while(a):
            n = n+ (a % 10)
            a=a // 10
        print(f"The sum of digits of {b} are {n}")
            
    except ValueError:
        print("Invalid input")
        
if __name__ == "__main__":
    sum()
            
            