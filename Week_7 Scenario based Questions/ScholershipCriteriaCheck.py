n = int(input())
eligibe = 0

for i in range(n):
    marks, attandance = list(map(int, input().split()))

    if(marks >= 80 and attandance >= 90):
        eligibe+=1
        
print(eligibe)
    