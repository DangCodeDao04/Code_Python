def la_so_hoan_hao(n):
    tong_uoc = 0
    for i in range(1,n):
        if n % i == 0:
            tong_uoc += i
    return tong_uoc == n   
n = int(input("Nhập số nguyên dương n:"))
if la_so_hoan_hao(n):
    print(f"Là số hoàn hảo")
else:
    print(f"Không phải số hoàn hảo")