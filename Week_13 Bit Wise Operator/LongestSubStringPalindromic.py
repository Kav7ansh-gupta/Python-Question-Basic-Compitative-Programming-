s = str(input())
answer = 1
for i in range(len(s)):
    for j in range(i,len(s)):
        s1 = s[i:j]
        if s1 == s1[::-1] and len(s1) > answer:
            answer = len(s1)
            
print(answer)
