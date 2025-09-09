arr = list(map(int,input().split()))
incrementValue = int(input("Enter the increment value : "))
updatedArr=[]

for i in arr:
    updatedArr.append(i+incrementValue)
print(f"The array before increment ; {arr}")
print(f"The array after increment ; {updatedArr}")