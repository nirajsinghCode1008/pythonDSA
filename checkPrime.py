def countVowel(count):
    count1=count.count("a")
    print("a =",count1)
    count1=count.count("e")
    print("e =",count1)
    count1=count.count("i")
    print("i =",count1)
    count1=count.count("o")
    print("o =",count1)
    count1=count.count("u")
    print("u =",count1)
    sum=(count1+count1+count1+count1+count1)
    return sum

    
    
count=input() 
   
countVowel(count)
