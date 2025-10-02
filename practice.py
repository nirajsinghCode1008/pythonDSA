def hcf_find (x,y):
    while x !=0 :
        x,y = y , x % y
    return x 
    
a= int(input("enter a number: "))
b= int(input("enter 2nd number: "))
print("The highest common factor of is",hcf_find(a,b))

