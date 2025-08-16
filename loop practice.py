#print 1 to 10 using a loop
'''
i=1
while i <= 10:
    print(i)
    i += 1   


#print even between 1 to 20
n=1
while n <= 20:
    if(n %2 == 0):
        print(n)
    n+=1  
       

#find the sum of number from 1 to 100 using a while
n=1
while n <= 100:
    sun=n*(n+1)//2
    n +=1
print(sun)
'''



# for loop practice test

#ques 1 print a number from 1 to 10 using for loop
for eng in range (1,11):
    print(eng,end=", ")


# print the even number from 1 to 20 in one line in for loop
for i in range (20):
    if i%2==0:
        print(i,end=" ")


#loop through the string "hello"and print each character on a #newline  
'''varau ="hello"
for char in varau:
    print("\n",char)
 '''
#print the multiplication table of a number by the user
'''num =int(input(" \n enter the number :"))
for i in range(1,11):
    print(i*num)'''

#sum form  1 to 100 
sum = 0
for i in range (1, 101):
    sum = sum + i 

    print(sum)


def firstAndLastSum(arr):
    ans = arr[0] + arr[-1]
    return ans 


arr = [1,2 ,4 ]
res = firstAndLastSum(arr)
print(res)


'''Given two integers X and N, print the value X on the screen N times. Move to the next line after printing, even if N = 0.'''

#Input: X = 7, N = 5

#Output: 7 7 7 7 7
x = 7
N = 5
i=0
while i < N:
    print(x,end=" ")
    i+=1




# how to revese it in function 
def digitize(n):
    result=0
    while n !=0:
        lastnumber=n%10  # get last number as remainder 
        
        result=result*10 + lastnumber       #
        n = n //10
    
    return result

n=35231
print(digitize(n))




# prnit the infinite loop until the user don't given the exit command .
while True:
    input_user= input("enter your string :")
    if input_user=="exit":
        break
        print("congratulatiom you guess the right one to stop this")
    print("the loop is continuing",input_user)    
    

