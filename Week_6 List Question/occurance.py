arr = list(map(int,input().split()))
target = int(input("Enter a the targetd number : "))
count = 0

for i in arr:
    if i == target:
        count+=1
print(f"The occurance of {target } in array : {arr} is : {count}")