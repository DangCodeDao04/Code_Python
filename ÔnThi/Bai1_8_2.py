def tinh_tong(n):
    s = 0
    for i in range(1,n+1):
        s += 1/(i**2+((i+1)**2))
        return s
n = int(input("Nhập số nguyên N:"))
print("Tổng S = (1/2)^2+(2/3)^2+...+(n/(n+1))^2 là:",tinh_tong(n))