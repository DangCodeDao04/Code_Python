import math
n = int(input("Nhập số nguyên n:"))
s = 1-pow(2,2)
for i in range(1,n+1):
    s = s+pow(-1,n-1) *pow(n,2)

print(f"Tổng của là:",{s})
