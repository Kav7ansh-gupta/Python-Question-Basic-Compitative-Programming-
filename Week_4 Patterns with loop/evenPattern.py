num = int(input("Enter a number : "))
value=1
for i in range(num):
    for j in range(i):
        print(value,end="")
        value+=1
    print()