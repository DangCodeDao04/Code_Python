def tinh_tong(n):
    s=0
    for i in range(1,n+1):
        s += 1/i
    return s
n = int(input("Nhập số nguyên dương n:"))
print("Tổng S = 1+1/2 +1/3+...+1/n là:",tinh_tong(n))

    