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
    
    