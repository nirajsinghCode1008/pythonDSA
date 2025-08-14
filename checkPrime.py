#checking the prime number and retun true and false if it is prime
def checkPrimenumber(number):
    if number==0:
        return 1
    factorial=1
    for i in range(1,number +1):
        factorial *= i
    print(factorial)
    
    
number= int(input())

checkPrimenumber(number)

