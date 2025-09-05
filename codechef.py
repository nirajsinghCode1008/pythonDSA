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

    