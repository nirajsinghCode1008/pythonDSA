#write a program to check if a list contain a palindromeof elements .hint(use copy method())
element=["apple","ball","appe"]
element1=element.copy()
element1.reverse()
if(element==element1):
    print("yes it is palindrone")
else:
    print("no it is not palindrone")    

#taking a input from user  three inpura,b,c crate alist and append into that list
variable=input("enter 1st letter: ")
variable1=input("enter 2nd letter: ")
variable2=input("enter 3rd letter: ")
variable3=variable+variable1+variable2
variable4=list(variable3)
variable4.append("a")
variable4.append("b")
variable4.append("c")
print(variable4)



