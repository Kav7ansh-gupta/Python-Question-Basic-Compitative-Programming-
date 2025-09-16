arr = list(map(int,input().split()))
target = int(input("Enter the number you wanted to search : "))

for i in arr:
    if i == target:
        print(f"The index of {target} is : {arr.index(i)}" )
    else:
        continue