n = int(input())
if n==1:
    print(1)
else:    
size = 2 * n-1
for i in range(1, size+1):
    for j in range(1, size+1):
        if i==1 or j==1 or i==2*n-1 or j==2*n-1  :
            print(n,end=" ")
        elif i==2 or j==2 or i==2*n-2 or j==2*n-2 :
            print(n-1,end=" ")
        elif i==3 or j==3 or i==2*n-3 or j==2*n-3 :
            print(n-2,end=" ")
        elif i==4 or j==4 or i==2*n-4 or j==2*n-4 :
            print(n-3,end=" ")
        elif i==5 or j==5 or i==2*n-5 or j==2*n-5 :
             print(n-4,end=" ")        
        else:
            print()
    print()        