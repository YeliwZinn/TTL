import math
def cir():
    a=float(input("Enter a radius :- "))
    
    try:
        r= math.pi*a*a
        print(f"The area of circle of radius{a} is {r}")
    
    except ValueError:
        print("Invalid input. Please enter numeric value.")
        
if __name__=="__main__":
    cir()