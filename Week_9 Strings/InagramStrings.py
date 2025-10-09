str1 = input()
str2 = input()
output = True
if len(str2)!=len(str1):
    print("Strings are not Inagram strings.")
else:
    sortedStr1 = sorted(str1)
    sortedStr2 = sorted(str2)

    for i in range(len(str1)):
        if sortedStr1[i] != sortedStr2[i]:
            output = False
            break
        else:
            output = True
print(f"Strings are Inagram : {output}")

