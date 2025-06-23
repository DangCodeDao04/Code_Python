def tinh_tong(n):
    s = 0
    for i in range(1,n+1):
        s += (2 *i)**2
    return s
n = int(input("Nhập số nguyên a:"))
print("Tính tổng S = 1+2^2+4^2+..2n^2",tinh_tong(n))