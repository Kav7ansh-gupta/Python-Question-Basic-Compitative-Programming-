n = int(input("Enter a number: "))

for i in range(n):
    print("*",end="")
    for j in range(n+1-i):
        print(" ",end="")
    print("*",end="")
    print()