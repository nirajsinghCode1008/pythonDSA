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


    


    