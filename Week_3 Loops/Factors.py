num = int(input("Enter a Number : "))
divide = 1
output = []

while divide<=num:
    if num%divide == 0:
        output.append(divide)
    divide+=1
print(f"The inputed number{num} is divisible by all this numbers : {output}")