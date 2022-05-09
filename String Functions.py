#list functions
str1=input("Enter a list")
print("1. Captalize"
      "\n2. Convert to lowercase"
      "\n3. Center the string"
      "\n4. Count the number of times the given value in string"
      "\n5. Encode"
      "\n6. Check if string ends with specific value"
      "\n7. set tab size of string"
      "\n8. search the string"
      "\n9. find index of given value"
      "\n10. Check if all characters are alphanumeric"
      "\n11. Check if all characters are alphabets"
      "\n12. Check if all characters are in lower case"
      "\n13. Check if all characters are numeric"
      "\n14. Check if all characters are printable"
      "\n15. Check if all characters are whitespaces"
      "\n16. Check if the string is a title"
      "\n17. Check if all characters are in upper case"
      "\n18. Add an iterable"
      "\n19. Get a left justified version of the string"
      "\n20. Get a left trim version of the string"
      "\n21. Get a tuple where string is divided into three parts"
      "\n22. Replace"
      "\n23. Get a right justified version of the string"
      "\n24. Split the string"
      "\n25. Check if string starts with a given value"
      "\n26. Swap Cases"
      "\n27. Convert into title case"
      "\n28. Convert string to upper case"
)

while True:
    n=int(input("Enter number point to gain above information on the string: "))
    if n==1:
       print(str1.capitalize())
    elif n==2:
        print(str1.lower())
    elif n==3:
        x=int(input("Amount of space (in character): "))
        print(str1.center(x))
        
    elif n==4:
        x=input("Value: ")
        print(str1.count(x))
      
    elif n==5:
        print(str1.encode())
       
    elif n==6:
        x=input("Value: ")
        print(str1.endswith(x))
        
    elif n==7:
        x=int(input("Tabspace: "))
        print(str1.expandtabs(x))
        
    elif n==8:
        x=input("Value: ")
        print(str1.find(x))
        
    elif n==9:
        x=input("Value: ")
        print(str1.index(x))
    elif n==10:
        print(str1.isalnum())
    elif n==11:
       print(str1.isalpha())
        
    elif n==12:
        print(str1.islower())

    elif n==13:
        print(str1.isnumeric())

    elif n==14:
        print(str1.isprintable())


    elif n==15:
        print(str1.isspace())
    elif n==16:
        print(str1.istitle())

    elif n==17:
        print(str1.isupper())

    elif n==18:
        x=eval(input("Tuple: "))
        print(",".join(x))
        
    elif n==19:
        x=int(input("Amount of space (in character): "))
        print(str1.ljust(x))

    elif n==20:
        print(str1.lstrip())

    elif n==21:
        x=input("where to partition: ")
        print(str1.partition(x))
        
    elif n==22:
        y=input("Value to replace")
        x=input("Value: ")
        
        print(str1.replace(y,x))
    elif n==23:
        x=int(input("Amount of space (in character): "))
        print(str1.rjust(x))
        
    elif n==24:
        x=input("where to split: ")
        print(str1.rsplit(x))
        
    elif n==25:
        x=input("Value: ")
        print(str1.startswith(x))
        
    elif n==26:
        print(str1.swapcase())
        
    elif n==27:
        print(str1.title())
        
    elif n==28:
        print(str1.upper())

    

        
        

    y_n=input("Do you want more info (yes/no): ")
    if y_n=="yes":
        pass
    else:
        break
