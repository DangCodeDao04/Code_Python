import math
def so_chinh_phuong(n):
    can = int(math.sqrt(n))
    return can * can == n
n =int(input("Nhập số nguyên n:"))
print("Số Chính Phương là:",so_chinh_phuong(n))
