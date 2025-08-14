#checking the prime number and retun true and false if it is prime
def checkPrimenumber(number):
    
    
    if number%1 == 0 and number //number== 0:
        print(True)
    else:
        print(False)  
    
number= int(input())

checkPrimenumber(number)

