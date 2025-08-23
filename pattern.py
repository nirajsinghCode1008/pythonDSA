"""#print the pattern like
*****
****
***
**
*
"""
num=5

for i in range(num):
    for j in range(num-i):
        print("*",end=" ")
    print()



"""write a program to print a pattern
*****
*****   
*****   
*****   
*****   
*****   
"""
num=5

for i in range(num):
    for j in range(num):
        print(" *",end=" ")
    print()


"""print a pattern like    
*
**
***
****
*****"""
num=5

for i in range(num):
    for j in range(i+1):
        print(" *",end=" ")
    print()    
#num+=1


"""write a program to print a pattern like
     *
    **
   ***  
  ****
 ***** """
num=5
for i in range(num):
    for j in range(i,num):
        print(" ",end=" ")
    for j in range(i+1):
        print("*",end=" ")    
    print()    
#num+=1


"""
write a program to print a pattern like
 *****
  ****
   ***
    **
     * """ 
num=5
for i in range(num):
    for j in range(i+1):
        print(" ",end=" ")
    for j in range(num-i):
        print("*",end=" ")    
    print()    
#num+=1



"""#write program to print the star like this
 **********
  ********
   ******
    ****
     **"""
num=5
for i in range(num):
    for j in range(i):
        print(" ",end=" ")
    for j in range(num-i ):
        print("*",end=" ") 
    for j in range(num-i ):
        print("*",end=" ")       
    print()    
    
""""
#write program to print the star like this
 *********
  *******
   *****
    ***
     *
"""
num=5
for i in range(num):
    for j in range(i):
        print(" ",end=" ")
    for j in range(num-i ):
        print("*",end=" ") 
    for j in range(num-1-i ):
        print("*",end=" ")       
    print()    