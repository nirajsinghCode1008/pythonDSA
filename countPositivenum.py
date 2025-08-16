#write a function to count the positive number
number=[2,-2,-5,7,8,-3,14,10]
def findpositive(number):
    count=0
    for i in range(len(number)):
        if number[i] > 0:
            count+=1
    print(count)
        

findpositive(number)        

    