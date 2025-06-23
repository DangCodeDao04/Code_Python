def tinh_tong(n):
    s = 0
    for i in range(1,n+1):
        s +=( (-1) **i)*(i ** 2)
    return s
n = int(input("Nhập số nguyên dương n:"))
print("Tổng là:",tinh_tong(n))