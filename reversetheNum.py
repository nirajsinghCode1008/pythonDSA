#write a function to reverse the number 

def reverseNum(num):
    count=0
    digit=len(str(num))
    for i in range(digit):
        num1 = num % 10
        count=count*10+num1
        num=num//10
    return count    
num =int(input())
print(reverseNum(num))