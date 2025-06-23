import math
def so_nguyen_duong(n):
    a = int(math.sqrt(n))
    return a
n = int(input("Nhập số nguyên a:"))
print("Số nguyên dương lớn nhất và m^2 <= n là:",so_nguyen_duong(n))