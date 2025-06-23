def uoc_lon_nhat(n):
    for i in range (n - 1 , 0, -1):
        if n % i == 0:
            return i
n = int(input("Nhập số nguyên dương n:"))
print("Ước số lớn nhất của", n, "là:", uoc_lon_nhat(n))