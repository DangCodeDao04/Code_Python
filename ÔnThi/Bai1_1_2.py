#1_1_2.2. Tính tổng S = 1/2 - 2/3 + ... + (-1)^n(n-1)/n.
def tinh_tong(n):
    if n >= 3:
         tong = 0
         for k in range(2,n+1):
             tong += ((-1) **k) * (k-1)/k
             return tong        
n = int(input("Nhập số nguyên dương n:"))
print("Tổng S = 1/2 - 2/3 + ... + (-1)^n(n-1)/n là:", tinh_tong(n))