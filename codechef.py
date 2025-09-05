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

    """Chef has 

X 5 rupee coins and 
Y 10 rupee coins. Chef goes to a shop to buy chocolates for Chefina where each chocolate costs 
Z rupees. Find the maximum number of chocolates that Chef can buy for Chefina.
    """
    t = int(input())

while t > 0:
    x, y, z = map(int, input().split())
    # Your code goes here
    t -= 1
    totalCoin = (5*x+10*y)
    
    totalchoclate=totalCoin // z
    
    print(totalchoclate)

    """Problem Statement
Write a program that accepts sets of three numbers, and prints the second-maximum number among the three.
    """
    n = int(input())
for _ in range(n):
    nums = list(map(int, input().split()))
    nums.sort()
    print(nums[1])
   
   """
   Chef wants to become fit for which he decided to walk to the office and return home by walking. It is known that Chef's office is 
X
X km away from his home.

If his office is open on 
5
5 days in a week, find the number of kilometers Chef travels through office trips in a week.
   """
    
    
    


    


    