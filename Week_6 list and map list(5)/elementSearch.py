arr = list(map(int,input().split()))
target = int(input())
for i in arr:
    if i == arr:
        print(f"The {target} is present in the array.")
    else:
        print(f"The {target} is not present in the array.")