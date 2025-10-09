str =input()
count = 0
for i in range(len(str)):
    tempStr = ""
    for j in range(i,len(str)):
        tempStr += str[j].lower()
        if tempStr[0] == 'a' or tempStr[0]=='e' or tempStr[0]=='i'or tempStr[0]=='o' or tempStr[0]=='u':
            count+=1
print(count)