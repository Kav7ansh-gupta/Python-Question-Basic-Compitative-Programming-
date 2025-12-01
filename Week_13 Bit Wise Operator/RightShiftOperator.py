# Given n an i check the i th bit is set or not set = 1 unset = 0
i = int(input())
target = int(input())
target = target >> i

if target == 1 :
    print("Set")
else:
    print("Unset")
    
    
    
    
    