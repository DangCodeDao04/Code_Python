def so_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False 
        return True
n = int(input("Nhập số nguyên n:"))

if n < 2:
    print("Vui lòng bạn nhập sô nguyên lớn hơn 2")
else:
    if so_nguyen_to(n):
        print(f"Là số nguyên tố")
    else:
        if so_nguyen_to(n):
    print(f"Không phải số nguyên tố")