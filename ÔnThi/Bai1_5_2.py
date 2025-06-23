def tinh_tong(n):
    s = 0
    for i in range(1,2 *n + 2,2):
        s += i**2
    return s
n = int(input("Nhập số nguyên dương n:"))
print("Tổng S = 1+3^2 +5^2+...+(2n+1)^2 là: ",tinh_tong(n))
