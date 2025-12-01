def VowelsVsConsonants(n):
    arr = []
    for i in range(n):
        Vowel = 0 
        Consonant = 0
        Str = input()
        for j in Str:
            if j.lower() == "a" or j.lower() == "e" or j.lower() == "i" or j.lower() == "o" or j.lower() == "u":
                Vowel += 1
            else :
                Consonant += 1
        arr.append([Vowel,Consonant])
    for i in range(len(arr)):
        for j in range(len(arr)):
            print(arr[i][j],end=" ")
        print()
        
n = int(input())        
VowelsVsConsonants(n)