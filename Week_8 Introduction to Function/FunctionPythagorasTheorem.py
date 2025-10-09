def PythagorasTheoram(height,base,perpe):
    a= height*height
    b= base*base
    c= perpe*perpe
    if (a+b)==c:
        return True
    else:
        return False
height = int(input())
base = int(input())
prepe = int(input())

ans = PythagorasTheoram(height,base,prepe)
print("PythagorasTheoram :",ans)