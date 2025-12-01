def sumAllNeturalNumbers(n):
    if (n ==1):
        return 1
    return (sumAllNeturalNumbers(n-1)+n)





n = int(input())
sum = 0

for i in range(1,n+1):
    sum+=i
print(sum)


print(sumAllNeturalNumbers(n))