import math
def tim_so_nguyen_duong(n):
    a = int(math.sqrt(n))
    return a
n = int(input("Nhập số nguyên dương n:"))
print("Số nguyên dương lớn nhất và m^2 <= n là:",tim_so_nguyen_duong(n))