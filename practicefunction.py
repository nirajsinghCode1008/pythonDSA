"""write a program to create a calculator that can perform at least five different mathematics operation such as addition, subtraction,multiplication ,division and average.ensure that the program is user-friendly,promption from input and display the results clearly."""
numA=int(input())
numB=int(input())
def calculatorAdd(numA,numB):
    print(numA+numB)
def calculatorSubtraction(numA,numB):
    print(numA-numB)
def calculatorMultiplication(numA,numB):
    print(numA*numB) 
def calculatorDivision(numA,numB):
    print(numA/numB) 
    
def calculatorAverage(numA,numB):
    print((numA+numB)/2)
    
    
calculatorAdd(numA,numB)
calculatorSubtraction(numA,numB)
calculatorMultiplication(numA,numB)
calculatorDivision(numA,numB)
calculatorAverage(numA,numB)
    

numA=int(input())
numB=int(input())
def calculatorAdd(numA,numB):
    sum=numA+numB
    return sum 
def calculatorSubtraction(numA,numB):
    subtract=numA-numB
    return subtract
def calculatorMultiplication(numA,numB):
    multiple=numA*numB
    return multiple
def calculatorDivision(numA,numB):
    division=numA/numB
    return division
    
def calculatorAverage(numA,numB):
    average=(numA+numB)/2
    return average
    
sum=calculatorAdd(numA,numB)   
print(sum)
subtract=calculatorSubtraction(numA,numB)  
print(subtract)
multiplication=calculatorMultiplication(numA,numB)  
print(multiplication)
division=calculatorDivision(numA,numB)  
print(division)
average=calculatorAverage(numA,numB)  
print(average)







numA=int(input())
numB=int(input())
def calculatorAdd(numA,numB):
    sum=numA+numB
    return sum 
def calculatorSubtraction(numA,numB):
    subtract=numA-numB
    return subtract
def calculatorMultiplication(numA,numB):
    multiple=numA*numB
    return multiple
def calculatorDivision(numA,numB):
    division=numA/numB
    return division
    
def calculatorAverage(numA,numB):
    average=(numA+numB)/2
    return average

variable=int(input()) 

match variable:
    case 1:
        sum=calculatorAdd(numA,numB)   
        print(sum)
    case 2: 
        subtract=calculatorSubtraction(numA,numB)  
        print(subtract)
    case 3:
        multiplication=calculatorMultiplication(numA,numB)  
        print(multiplication)
    case 4:    
        division=calculatorDivision(numA,numB)  
        print(division)
    case 5:    
        average=calculatorAverage(numA,numB)  
        print(average)
    case _ :
        print("Wrong request")