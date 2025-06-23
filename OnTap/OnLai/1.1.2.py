def tinh_tong(n):
    s = 0
    for i in range(n):
        s += (((-1) ** n *(n-1/n)))
    return s
n = int(input("Nhập số nguyên n:"))
print("Tính tổng S = 1/2 -2/3+...+(-1)^nn-1/n là:",tinh_tong(n))
