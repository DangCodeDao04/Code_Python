import math
def so_chinh_phuong(n):
    can = int(math.sqrt(n))
    return can * can == n
n = int(input("Nhập số nguyên n:"))
print("Tổng các số chính phương là:",so_chinh_phuong(n))
