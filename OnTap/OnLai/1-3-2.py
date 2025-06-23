def tinh_tong(n):
    s = 0
    for i in range(n):
        s += (((-1)**n-1) * (n**2))
    return s
n =int(input("Nhập số nguyên n:"))
print("Tính tổng S = 1-2^2+...(-1)^n.n^2 là:",tinh_tong(n))
