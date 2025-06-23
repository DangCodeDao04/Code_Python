import math
n = int(input("Nhập số nguyên của a:"))
s = 1/2   
for i in range(3,n+3):
    s = s + math.pow(1,i) * (i-1)/i
print("Tổng của S = 1/2 -2/3+...:",{s})

    