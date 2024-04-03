def perf():
    a=int(input("Enter a no. :-")) 
    x=0
    for i in range(1,a):
        if (a % i) == 0:
            x = x + i
                      
    if x==a:
        print(f"{a} is a perfect.")
    else:
        print(f"{a} is not perfect.")
        
if __name__ == "__main__":
    perf()