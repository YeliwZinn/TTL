def fib(n):
    seq=[0,1]
    
    for i in range(2,n):
        x=seq[i-1]+seq[i-2]
        seq.append(x)
        
    return seq[:n]

def find():
    n=int(input("Enter a no. :-"))
    
    r=fib(n)
    print(f"The seq{r}")
    
if __name__ == "__main__":
    find()