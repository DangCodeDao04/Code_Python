def so_hoan_hao(n):
    so_hoan_hao = 0
    for i in range(2,n):
        if n % i ==0:
            so_hoan_hao += i
    return so_hoan_hao == n
n = int(input("Nhập số nguyên n:"))
if so_hoan_hao(n):
    print("Là số hoàn hảo")
else:
    print("Không phải số hoàn hảo")