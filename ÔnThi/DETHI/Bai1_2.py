def tinh_tong(n):
    s = 0 
    for i in range(2,n+1):
        s+= ((-1)**i) *((i-1)/i)
    return s
n = int(input("nhập số nguyên n:"))
print("Tính tổng S = 1/2 - 2/3 +....+(-1)^n n-1/n là:",tinh_tong(n))