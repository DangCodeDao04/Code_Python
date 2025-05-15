#Kiểm tra số nguyên tố

def la_so_nguyen_to(n):
    if (n < 2):
        return false
    for i in range(2, int(n ** 0.5)+1):
        if (n % i == 0):
            return False
        return True

n = int(input("Nhập số nguyên dương:"))
if la_so_nguyen_to(n):
    print(n,"là số nguyên tố")
else:
    print(n,"Không phải số nguyên tố.")
    
