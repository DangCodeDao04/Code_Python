def tinh_tong(n):
    tong = 0
    for i in range(n):
        tong += n % 10
        n // 10
    return tong
n = int(input("Nhập số nguyên n:"))
print("Tính tổng các chữ số của n:",tinh_tong(n))
   