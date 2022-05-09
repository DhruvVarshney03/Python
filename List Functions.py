#list functions
l1=eval(input("Enter a list"))
print("1. print \n2. Number of items \n3. To check type() of the item \n4. Check if the item is in the list \n5. Insert \n6. Append \n7. Add a list (Extend) \n8. Remove using item name"
      "\n9.Remove using index \n10. Clear the list \n11. sort (Ascending) \n12. Sort (Descending)")

while True:
    n=int(input("Enter number point to gain above information on the string: "))
    if n==1:
        print(l1)
    elif n==2:
        print(len(l1))
    elif n==3:
        print(type(l1))
    elif n==4:
        n1=int(input("Enter the item name: "))
        if n1 in l1:
            print("yes,",n1,"is in the list")
    elif n==5:
        n1=int(input("Enter the number you want to insert: "))
        n2=int(input("Enter the index: "))
        l1.insert(n2,n1)
        print(l1)
    elif n==6:
        n1=int(input("Enter the number you want to append: "))
        l1.append(n1)
        print(l1)
    elif n==7:
        l2=eval(input("Enter the list"))
        l1.extend(l2)
        print(l1)
    elif n==8:
        n1=int(input("Enter the number you want to remove: "))
        l1.remove(n1)
        print(l1)
    elif n==9:
        n2=int(input("Enter the index you want to remove: "))
        c=input("Do you want use pop or del? ")
        if c=="pop":
            l1.pop(n2)
            print(l1)
        else:
            del l1[n2]
    #elif n==10:
        #print(l1.clear())
    elif n==11:
        l1.sort()
        print(l1)
    elif n==12:
        l1.reverse()
        print(l1)
        

    y_n=input("Do you want more info (yes/no): ")
    if y_n=="yes":
        pass
    else:
        break
