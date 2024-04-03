def power(x,y):
    return x**y

def find():
    x=int(input("Enter a no. :- "))
    y=int(input("Enter the power:- "))
    
    try:
        r=power(x,y)
        print(f"The result is {r}")
    except ValueError:
        print("Invalid value")

if __name__=="__main__":
    find()