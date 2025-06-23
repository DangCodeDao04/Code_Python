import math
def so_chinh_phuong(n):
    can = int(math.sqrt(n))
    return can * can
n= int(input("Nhập số nguyên n:"))
print("Kiểm tra phải số chính phương không là:",so_chinh_phuong(n))
9