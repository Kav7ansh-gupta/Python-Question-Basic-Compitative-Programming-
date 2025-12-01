# def SubArrayLessthenB(arr , b):
#     count = 0
#     for i in range(len(arr)):
#         for j in range(i,len(arr)):
#             output=[]
#             for k in range(i,j+1):
#                 output.append(arr[k])
#             intsum = sum(output)
#             if intsum <b:
#                 count+=1
#     return count

# arr = list(map(int,input().split()))
# b = int(input())
# print(SubArrayLessthenB(arr,b))

arr = [1,2,3,4,5,6,7,8,9]

subarrays = []
for i in range(len(arr)):     
    subarrays.extend([sum(arr[i:j]) for j in range(i+1, len(arr)+1)])
maximum = max(subarrays)
    

print(subarrays)
print(maximum)
