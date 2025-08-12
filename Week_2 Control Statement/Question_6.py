# Q6 Read three integers and print their maximum.
Number_1 = int (input("Enter the Number 1 : "))
Number_2 = int (input("Enter the Number 2 : "))
Number_3 = int (input("Enter the Number 3 : "))

if (Number_1>Number_2 and Number_1>Number_3):
    print(Number_1,"is the highest among all")
elif (Number_2>Number_1 and Number_2>Number_3):
    print(Number_2,"is the highest among all")
else:
    print(Number_3,"is the highest among all")
