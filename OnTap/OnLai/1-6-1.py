def tinh_tong(n):
    s = 0
    while n > 0:
        s += n %10
        n //=10
    return s
n = int(input("Nhập số nguyên n:"))
print("Tổng các chữ số của n là:",tinh_tong(n))