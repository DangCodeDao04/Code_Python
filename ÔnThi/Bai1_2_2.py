def tinh_tong(n):
    tong = 0
    for i in range(1,n+1):
        tong += 1/(i**2)
    return tong

n = int(input("Nhập số nguyên dương n:"))
print("S = 1/2 +1/2^2+...+1/n^2 là:",tinh_tong(n))