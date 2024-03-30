print (" mini calculator ")

a=float(input("enter the number : "))
b=float(input("enter the number : "))


print ("press 1 for addition")
print("press 2 for subtraction")
print("press 3  for multiplication")
print("press 4 for division")

choice=int(input("enter your choice : "))

if(choice in [1,2,3,4]):
    
    if choice == 1:
        print(a+b)
    elif choice == 2:
        print(a-b)
    elif choice == 3:
        print(a*b)
    elif choice == 4:
        if b==0.0:
            print("cannot be divided")
        else :
            print(a/b)


else:
    print("invalied input")


    print("the choice is {}".format(0))

