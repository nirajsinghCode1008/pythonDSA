#write a program to print  a given number is a leap year or not
def is_leap(year):
    if year%400==0 or (year%40==0 and year%100!=0):
        return True
    else:
        return False    
year = int(input())
print(is_leap(year))



