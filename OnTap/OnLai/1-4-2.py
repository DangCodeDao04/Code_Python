def tinh_tong(n):
    s = 0
    for i in range(1,2*n+1,2):
        s +=i**2
    return s
n =int(input("Nhập nguyên n:"))
print("Tính tổng S = 1+2^2 +4^2 +....+(2n)^2 là:",tinh_tong(n))
