def tinh_giai_thua(n):
    giai_thua = 1
    for i in range(2,n+1):
        giai_thua *= i
    return giai_thua
def tinh_tong(n):
    s = 0
    for i in range(2,n+1):
        s += 1/tinh_giai_thua(i)
    return s
n = int(input("Nhập số nguyên dương n:"))
