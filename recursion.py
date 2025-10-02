#write a program to print a number rom given range in #increasing order
def numberprint(num1,num2):
    if num1>num2:
        return
    print(num1)
    numberprint(num1+1,num2)
numberprint(1,5)    




#write a program to print a number rom given range in #dencreasing  order
def numberprint(num1,num2):
    if num1>num2:
        return
    numberprint(num1+1,num2)
    print(num1)
numberprint(1,5)    


#write a program to print "hello dabbu" for 999 times means infinite 
count=0
def is_leap():
    global count
    count +=1
    print("hello",count)
    is_leap()
    
is_leap()
     

#write a program to print "hello dabbu" for 100 times means infinite 
import sys
print(sys.getrecursionlimit())
sys.setrecursionlimit(201)
print(sys.getrecursionlimit())
count=0
def is_leap():
    global count
    count +=1
    print("hello",count)
    is_leap()
    
is_leap()
    
