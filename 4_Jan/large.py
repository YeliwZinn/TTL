def large():
    a=int(input("Enter a no. :- "))
    b=int(input("Enter another no. :-"))
    
    try:
        r=max(a,b)
        print(f"Between {a} and {b} the largest no. is {r}")
    except ValueError:
        print("Please enter a valid integer")
        
if __name__=="__main__":
    large()