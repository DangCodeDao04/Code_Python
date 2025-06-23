def so_hoan_hao(n):
    tong_uoc = 0
    for i in range(1,n):
        if n % i == 0:
            tong_uoc += i
        return tong_uoc == n
n = int(input("Nhập số nguyên n:"))
if so_hoan_hao(n):
    print("Là số hoàn hảo ")
else:
    print("Không phải số hoàn hảo")

