import math
n = int(input("Nhập số nguyên của n:"))
s = 1/2*2
for i in range(1, n+1):
    s = s + 1/pow(i,i)

print("Tổng:",{s})
