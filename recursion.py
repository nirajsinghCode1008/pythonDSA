#write a program to print a number rom given range in #increasing order
def numberprint(num1,num2):
    if num1>num2:
        return
    print(num1)
    numberprint(num1+1,num2)
numberprint(1,5)    
