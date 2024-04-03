def paisa():
    a=int(input("Enter the paisa u want :-"))
    
    try:
        r=a//100
        p=a%100
        
        print(f"The paisa {a} is {r}rupee and {p}paisa")
    except ValueError:
        print("Please enter a valid money.")
        
if __name__=="__main__":
    paisa()
        