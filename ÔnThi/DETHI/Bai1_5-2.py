def tinh_tong(n):
    s = 0
    for i in range(1,n+1):
        s+= ((2 * n + 1)**2)
    return s
n = int(input("Nhập số nguyên n:"))
print("Tính Tổng S = 1 + 3^2 +5^2 + ... + (2n+1)^2 là:",tinh_tong(n))
