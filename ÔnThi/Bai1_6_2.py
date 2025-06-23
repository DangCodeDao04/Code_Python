def tinh_tong(n):
    S = 0
    for i in range(1,n+1):
        S += 1/(i*(i+1))
    return S
n = int(input("Nhập số nguyên dương n:"))
print("Tổng S = 1/1.2 +1/2.3+...+1/n.(n+1) là:",tinh_tong(n))