n = int(input())
arr = list(map(int,input().split()))

max= float("-inf")
min = arr[0]

for i in arr:
    if i>max:
        max=i
    if i<min:
        min=i
print(max,min)