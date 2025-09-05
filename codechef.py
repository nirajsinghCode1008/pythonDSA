"""Sum of Digits
You're given an integer N. Write a program to calculate the sum of all the digits of N.
"""
# cook your dish here 
t=int(input())
for _ in range(t):
    #print()
    count=0
    n=int(input())
    while n>0:
        result=n%10
        count=count+result
        n=n//10
    print(count)

    """Scalene Triangle
Given 
A,B and
C as the sides of a triangle, find whether the triangle is scalene.
    """
    t = int(input())

while t > 0:
    a, b, c = map(int, input().split())
    # Your code goes here
    t -= 1
    if a!=b!=c:
        print("YES")
        
    else:
        print("NO")


"""
Candy Store
Chef has started working at the candy store. The store has 
100
100 chocolates in total.

Chef’s daily goal is to sell 
X
X chocolates. For each chocolate sold, he will get 
1
1 rupee. However, if Chef exceeds his daily goal, he gets 
2
2 rupees per chocolate for each extra chocolate.

If Chef sells 
Y
Y chocolates in a day, find the total amount he made.
"""
t = int(input())

while t > 0:
    x, y = map(int, input().split())
    # Your code goes here
    t -= 1
    
    extra_choc=y-x
    profit_extra_choc=extra_choc*2
    
    if y<x:
        print(y)
    else:
        print(x+profit_extra_choc)
    
    
"""Find Remainder
Write a program to find the remainder when an integer A is divided by an integer B.
"""
t=int(input())
while t>0:
    A,B = map(int,input().split())
    
    t-=1
    reminder=A%B
    print(reminder)
    
    


    


    