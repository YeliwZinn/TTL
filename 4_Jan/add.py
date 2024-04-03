def add():
    a= int(input("Enter a no. :- "))
    b=int(input("Enter another no. :-"))
    
    try:
        res=a+b
        print(f"The addition result is {res}")
    
    except ValueError:
        print("Enter a numerical value")
    

if __name__=="__main__":
    add()
    
        