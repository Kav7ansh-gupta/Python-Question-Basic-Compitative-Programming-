def loopBinarysearch(arr,target):
    lower = 0
    high = len(arr)
    while(lower<=high):
        mid = (lower+high)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            lower = mid +1
        else:
            high = mid + 1
def RecursiveBinarysearch(arr,lower,high,target):
    if lower > high:
        return -1
    mid = (lower+high)//2
    if arr[mid] == target:
        return mid
    elif arr[mid]< target :
        return RecursiveBinarysearch(arr,mid+1,high,target)
    else :
        return RecursiveBinarysearch(arr,lower,mid-1,target)
            
    
    
arr = list(map(int,input().split()))
arr.sort()
target = int(input())
print(loopBinarysearch(arr ,target))
print(RecursiveBinarysearch(arr,0,len(arr),target))