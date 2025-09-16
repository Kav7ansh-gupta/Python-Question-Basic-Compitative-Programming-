arr = list(map(int,input("Enter the array elements : ").split()))
b = int(input())
copyOfArray =[]
for i in arr:
    copyOfArray.append(i+b)
print(copyOfArray)