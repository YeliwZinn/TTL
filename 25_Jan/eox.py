n = [1, 2, 3, 4, 5, 6, 7]
s=list(filter(lambda x:x %2==0,n))
print(s)

def eo(l):
    l=[a for a in l if a %2 ==0 ]
    print(l)
    
l=[1,2,3,4,5,6,7]
eo(l)