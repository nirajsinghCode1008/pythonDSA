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

    