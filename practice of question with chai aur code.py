#write a function to count the positive number
number=[2,-2,-5,7,8,-3,14,10]
def findpositive(number):
    count=0
    for i in range(len(number)):
        if number[i] > 0:
            count+=1
    print(count)
        

findpositive(number)        
       


       


number=[1,-2,3,-4,5,6,7,8,-3,14,10]
countpositivenumber=0
countnegativenumber=0
for i in number:
    if i > 0:
        countpositivenumber +=1
    elif i < 0:
        countnegativenumber +=1
print("the total number of positive number is:", countpositivenumber)        
print("the total number of negative number is:", countnegativenumber)        
    
    

# write a program to add the total even number from the given number
n=11
sumofeven=0
for i in range(n):
    if i % 2== 0:
        sumofeven=sumofeven + i
print(sumofeven) 



#write a program to find the number of even
n=10
sumofeven=0
for i in range(n):
    if i % 2!= 0:
        sumofeven += 1
print(sumofeven) 


#write a program to create a multiplication of number till 10

n=10
for i in range(1,n+1):
    if i==5:
        continue
    print(i,"x",n,"=",i*n)  


 #write a program to reverse a strinf from loop 
input_str="python"
reverse_num=" "
for char in input_str:
    reverse_num = char + reverse_num
    
print(reverse_num)   




# find the print non- repeated character
input_str="narayan prasad singh"

for char in input_str:
    
    if input_str.count(char) == 1:
         print('char is ',char)
         break
    

#factorial calculator
number=10
factorise=1
while number>0:
    factorise=factorise * number
    number -= 1
print("the factoril number is :",factorise)  


# vlid input 
#pronlem,keep asking the user for input until the enter a number betwwen 1 to 10

while True:
    number = int(input("enter your number betwwen 1 to 10:"))
    if 1<= number <= 10:
        print("thanks")
        break
    else:
        ("invalid nuber try again")    
    
     


#find the given number is prime or not
number=12
for i in range(2,number):
    if number%i==0:
        print("not prime")
        break
else:
    print("prime")
         
    

# exponents backoff
import time
attempt=0
max_retries=5
wait_time=1
while attempt<max_retries:
    print("attempt",attempt+1,"wait_time",wait_time,)
    time.sleep(wait_time)
    attempt +=1
    wait_time*=2
