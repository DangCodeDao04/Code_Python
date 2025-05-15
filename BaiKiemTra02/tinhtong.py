#tinh tổng S = 1/2 + 1/3 +1/4 +1/5 ....+1/n
def tinh_tong1n(n):
    tong = 0
    for i in range(n):
        tong += 1 / i
    return tong
 
n = 5
print(f"Tổng 1 + 1/2 + ... + 1/{n} là: {tinh_tong1n(n)}")

    