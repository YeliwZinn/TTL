def swap():
    a=int(input("Enter a no. :- "))
    b=int(input("Enter another no. :- "))
    print(f"a:{a}")
    print(f"b:{b}")
    
    try:
        a,b=b,a
        print(f"The swapped value of a is {a} and b is {b}")
        
    except ValueError:
        print("Invalid input")
        
if __name__=="__main__":
    swap()