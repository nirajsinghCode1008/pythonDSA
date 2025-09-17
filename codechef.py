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
   
"""Chef wants to become fit for which he decided to walk to the office and return home by walking. It is known that Chef's office is 
X
X km away from his home.

If his office is open on 
5
5 days in a week, find the number of kilometers Chef travels through office trips in a week.
   """
t = int(input())
while t > 0:
    x = int(input())
    t -= 1
    # Your code goes here
    totaldistance=2*x * 5
    print(totaldistance)

    """You are given an integer n. You need to check whether the number is a palindrome number or not. Return true if it's a palindrome number, otherwise return false.
A palindrome number is a number which reads the same both left to right and right to left.
    """
class Solution:
    def isPalindrome(self, n):
        counts = 0
        temp = n                   
        while n > 0:
            extract_num = n % 10
            counts = (counts * 10) + extract_num
            n = n // 10
        if counts == temp:          
            return True
        else:
            return False
    
       #or
n=334
counts=0
num=n
while n>0:
    extract_num=n%10
    counts=((counts*10)+extract_num)
    n=n//10
#print(counts)
if num == counts:
    print("True")
else:
    print("False")

"""You are given an integer n. You need to check whether it is an armstrong number or not. Return true if it is an armstrong number, otherwise return false.
An armstrong number is a number which is equal to the sum of the digits of the number, raised to the power of the number of digits.
    """
    
n=int(input())
num=n
counts=0
temp=n
while temp>0:
    temp=temp//10
    counts +=1

sum_num=0
temp=n
while temp>0:
    extract_num=temp%10
    sum_num +=extract_num**counts
    temp=temp//10
if sum_num==num:
    print("true")
else:
    print("false")
    # class Solution:
    def isArmstrong(self, n):
        num=n
        counts = len(str(n))
        sum_of_num=0
        while n>0:
            extract_num=n%10
            sum_of_num +=extract_num**counts
            n=n//10
        if sum_of_num==num:
            return True
        else:
            return False

"""You are given an integer n. You need to check if the number is a perfect number or not. Return true if it is a perfect number, otherwise, return false.

A perfect number is a number whose proper divisors (excluding the number itself) add up to the number it
""" 
class Solution:
    def isPerfect(self, n):
        num=n
        count=0
        temp=n
        for i in range(1,n):
            if temp%i==0:
                count=count+i
        if num==count:
            return True
        else:
            return False    



        """
        You are given two integers n1 and n2. You need find the Greatest Common Divisor (GCD) of the two given numbers. Return the GCD of the two numbers.



The Greatest Common Divisor (GCD) of two integers is the largest positive integer that divides both of the integers.


Examples:
Input: n1 = 4, n2 = 6

Output: 2

Explanation: Divisors of n1 = 1, 2, 4, Divisors of n2 = 1, 2, 3, 6

Greatest Common divisor = 2.
"""
class Solution:
    def GCD(self, n1, n2):
        if n2 > n1:
            mn=n1
        else:
            mn=n2
        for i in range(1,mn+1):
            if n1%i==0 and n2%i==0:
                GCD = i
        
        return GCD                        

"""You are given an integer n. You need to find all the divisors of n. Return all the divisors of n as an array or list in a sorted order.

A number which completely divides another number is called it's divisor.


Examples:
Input: n = 6
Output = [1, 2, 3, 6]
Explanation: The divisors of 6 are 1, 2, 3, 6.
"""            
class Solution:
    def divisors(self, n):
        null=[]
        for i in range(1,n+1):
            if n%i==0:
                null.append(i)
        return(null)
        

"""You are given two integers n1 and n2. You need find the Lowest Common Multiple (LCM) of the two given numbers. Return the LCM of the two numbers.

The Lowest Common Multiple (LCM) of two integers is the lowest positive integer that is divisible by both the integers.


Examples:
Input: n1 = 4, n2 = 6
Output: 12
Explanation: 4 * 3 = 12, 6 * 2 = 12.


12 is the lowest integer that is divisible both 4 and 6.
Input: n1 = 3, n2 = 5
Output: 15
Explanation: 3 * 5 = 15, 5 * 3 = 15.
15 is the lowest integer that is divisible both 3 and 5.

Input: n1 = 4, n2 = 12
Output:12
"""
class Solution:
    def LCM(self, n1, n2):
        if n2 > n1:
            mn=n1
        else:
            mn=n2
        for i in range(1,mn+1):
            if n1%i==0 and n2%i==0:
                hcf=i
            LCM= n1*n2//hcf 
        return LCM      
                            



        