def tinh_tong(n):
    tong = 0
    for i in range(1, n + 1):
        tong += float(1 / i)
    return tong

# Nhập số nguyên dương từ bàn phím
n = int(input("Nhập số nguyên dương n: "))
if n > 0:
    ket_qua = tinh_tong(n)
    print(f"Tổng S = {ket_qua}")
else:
    print("Vui lòng nhập số nguyên dương!")
2