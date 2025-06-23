n = int(input("Nhập số nguyên từ (0<n<100) là:"))
while n<=0 or n>=100:
    print("Giá trị không hợp lê.Vui lòng nhập lại")
    n = int(input("Nhập số nguyên từ (0<n<100) là:"))
day_so = []
for i in range(n):
    x =int(input(f"Nhập số phần tử thứ {i+1} là:"))
    day_so.append(x)
    
#Đếm số trong dãy có bao nhieu duong
so_duong = 0
for num in day_so:
    if num > 0:
        so_duong += 1
print("\n Danh sách trong dãy là số dương:",so_duong)

so_duong_min =0
for num in day_so:
    if num < 0:
        if so_duong_min == 0 or num < so_duong_min:
            so_duong_min = num
print("\n Danh sách số dương nhỏ nhất:",so_duong_min)