import math
def la_so_chinh_phuong(n):
    if n<0:
        return false
    a = math.isqrt(n)
    return a * a == n
n = int(input("Nhập số nguyên của n:"))
if la_so_chinh_phuong(n):
    print(f"Là số chính phương")
else:
    print(f"Không phải số chính phương")
    
