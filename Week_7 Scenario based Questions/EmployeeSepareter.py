n = int(input())
arr = list(map(int,input().split()))
odd = 0

for i in arr:
    if i %2 == 0:
        print(i,end=" ")
    else:
        odd+=1
if odd == len(arr):
    print(-1)