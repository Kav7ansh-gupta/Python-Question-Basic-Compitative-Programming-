arr = list(map(int,input().split()))
target = int(input("Enter the number you wanted to search : "))

for i in arr:
    if i == target:
        print(f"Yes the number {target} is available in list and it's index is {arr.index(i)}")
        break
    else:
        print("Number is not available")