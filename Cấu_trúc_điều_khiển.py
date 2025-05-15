#Câu lệnh if else 
a = int(input("Nhập số thứ nhất:"))
b = int(input("Nhập số thứ hai"))
if a > b:
    print(f"Số lớn hơn là:{a}")
elif a < b:
    print(f"Số lớn hơn là:{b}")
else:
    print("Hai số bằng nhau")
    
    
#Kiểm tra số chẵn lẻ
n = int(input("Nhập một số nguyên:"))
if n % 2 == 0:
    print(f"{n} là số chẵn")
else:
    print(f"{n} là số lẻ")
    