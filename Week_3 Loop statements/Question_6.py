Num = int(input("Enter a number : "))
i=1
sum = 0
while i<=Num:
    if i % 2 == 0:
        sum += i
    i+=1
print(f"The sum of all even numbers for {Num} is : {sum}")