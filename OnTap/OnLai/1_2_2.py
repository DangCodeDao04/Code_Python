def tinh_tong(n):
    s = 0
    for i in range(1,n+1):
        s+= 1/i**2
    return s
n = int(input("Nhập số nguyên n:"))
print("Tính tổng S = 1/1^1 +1/2^2 +...+1/n^2 là:",tinh_tong(n))
