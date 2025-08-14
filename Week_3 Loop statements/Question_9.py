num = int(input("Enter a number : "))
sum = 0
while num!=0:
    value = num%10
    num = num//10
    sum+=value
print(f"The Inputed number's all digit sum is : {sum}")