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



    """"
    #write program to print the star like this
         *
       * * *
     * * * * * 
   * * * * * * *
 * * * * * * * * *
"""
num=5
for i in range(num):
    for j in range(i,num):
        print(" ",end=" ")
    for j in range(i+1):
        print("*",end=" ") 
    for j in range(i):
        print("*",end=" ")       
    print()    



'''
write a program to print a pattern like this
1
12
123
1234
12345
'''
n=5
for i in range(1,n+1):
            for j in range(i):
                print(j+1,end=" ")
               
            print()


""""  
write a program to print a pattern like this
1
22
333
4444
55555
"""
n=5
for i in range(1,n+1):
            for j in range(i):
                print(i,end=" ")
               
            print()



'''
write a program to print a pattern like this
12345
1234
123
12
1
'''
n=5
for i in range(0,n+1):
    for j in range(n-i):
        print(j+1,end=" ")
    print()



    """
    Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:
    *
   ***
  *****
 *******
*********
Print the pattern in the function given to you.
    """
class Solution:
    def pattern7(self, n):
     for i in range(0,n):
        for j in range(n-i-1):
            print(" ",end="")
        for j in range(i+1):
            print("*",end="")
        for j in range(i):
            print("*",end="")    
        print()




""" 
Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:
*********
 *******
  *****
   ***
    *
Print the pattern in the function given to you.          
""" 
class Solution:
    def pattern8(self, n):
        for i in range(n):
            for j in range(i):
                print(" ",end="")
            for j in range((n-i)+(n-i)-1):
                print("*",end="")
            print()           


"""
Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:



    * 
   ***
  *****
 *******
*********
*********
 *******
  *****
   ***
    *
Print the pattern in the function given to you.
"""
def pattern9(self, n):
        for i in range(0,n):
            for j in range(n-i-1):
                print(" ",end="")
            for j in range(i+1):
                print("*",end="")
            for j in range(i):
                print("*",end="")    
            print()
        for i in range(0,n):
            for j in range(i):
                print(" ",end="")
            for j in range(n-i):
                print("*",end="")
            for j in range(n-i-1):
                print("*",end="")    
            print()
       

"""
iven an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:
*

**

***

****

*****

****

***

**

*
Print the pattern in the function given to you.
"""
class Solution:
    def pattern10(self, n):
        for i in range(1,n+1):
            print((i)*"*")
        for i in range(n-1):
            print((n-i-1)*"*")
            
"""
Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:



1 

0 1 

1 0 1 

0 1 0 1 

1 0 1 0 1
Print the pattern in the function given to you."""
class Solution:
    def pattern11(self, n):
        for i in range(1,n+1):
            for j in range(1,i+1):
                if (i+j)%2==0:
                    print(1,end=" ")
                else:
                    print(0,end=" ")
            print()        



"""
Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:



1        1
12      21
123    321
1234  4321
1234554321
Print the pattern in the function given to you."""
class Solution:
    def pattern12(self, n):
        for i in range(1,n+1):
            for j in range(i):
                print(j+1,end="")
            for j in range(n-i): 
                print("  ",end="")
            for j in range(i):
                 print(i-j,end="")
            print()    


"""
Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:



1 

2 3 

4 5 6 

7 8 9 10 

11 12 13 14 15
Print the pattern in the function given to you."""
class Solution:
    def pattern13(self, n):
        count =1
        for i in range(1,n+1):
            for j in range(i):
                print(count,end=" ")
                count+=1
            print()


"""
Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:



A

AB

ABC

ABCD

ABCDE
Print the pattern in the function given to you."""
class Solution:
    def pattern14(self, n):
        for i in range(65,n+65):
            for j in range(65,i+1):
                print(chr(j),end="")
                
            print()
            


"""        Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:



A

BB

CCC

DDDD

EEEEE
Print the pattern in the function given to you.""" 
class Solution:
    def pattern16(self, n):
        for i in range(65,n+65):
            for j in range(65,i+1):
                print(chr(i),end="")
            print()   


"""
Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:



    A
   ABA
  ABCBA
 ABCDCBA
ABCDEDCBA


Print the pattern in the function given to you."""
n=5
for i in range(n):
    for j in range(n-i-1):
        print(" ",end="")
    for k in range(i+1):
        print(chr(65+k),end="")
    for l in range(1,i+1):
        print(chr(65+i-l),end="")
    print()   



            #or


      
        #print the number of rows
for i in range(n):

    #printing spaces
    for j in range (n-i-1):
        print(" ",end="")
            
    #printing character
    ch = 'A'
    breakpioint=(2 * i +1)//2
    for j in range (1, 2 * i + 2):
        print(ch ,end="")
        if j <=breakpioint:
            ch = chr(ord(ch)+1)
        else:
            ch = chr(ord(ch)-1)
        
    print()
                  

"""Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:



E 

D E 

C D E 

B C D E 

A B C D E
Print the pattern in the function given to you."""
n=5
for i in range(1,n+1):
            #second loop describe the numner of colum or numner of value
        for j in range(i):
            print(chr(65+n+j-i),end=" ")
        print()



"""Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:



**********
****  ****
***    ***
**      **
*        *
*        *
**      **
***    ***
****  ****
**********
"""
n=5
for i in range(n):
    for j in range(n-i):
        print("*",end="")
    for k in range(2*i):
       print(" ",end="")
    for l in range(n-i):
       print("*",end="")
    print()
for i in range(1,1+n):
    for j in range(i):
        print("*",end="")
    for k in range(2*n-2*i):
       print(" ",end="")
    for l in range(i):
       print("*",end="")
    print()  

    """Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:



5 5 5 5 5 5 5 5 5 
5 4 4 4 4 4 4 4 5 
5 4 3 3 3 3 3 4 5 
5 4 3 2 2 2 3 4 5 
5 4 3 2 1 2 3 4 5 
5 4 3 2 2 2 3 4 5 
5 4 3 3 3 3 3 4 5 
5 4 4 4 4 4 4 4 5 
5 5 5 5 5 5 5 5 5
Print the pattern in the function given to you
""" 
n = int(input())
if n==1:
    print(1)
else: 
    size = 2 * n-1
    for i in range(1, size+1):
        for j in range(1, size+1):
            if i==1 or j==1 or i==2*n-1 or      j==2*n-1  :
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
           


"""Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:



*        *
**      **
***    ***
****  ****
**********
****  ****
***    ***
**      **
*        *

"""
n=5 
for i in range(1,1+n):
    for j in range(i):
        print("*",end="")
    for k in range(2*n-2*i):
        print(" ",end="")
    for l in range(i):
        print("*",end="")    
    print()
for i in range(1,1+n):
    for j in range(n-i):
        print("*",end="")
    for k in range(2*i):
        print(" ",end="")
    for l in range(n-i):
        print("*",end="")    
    print()                  
