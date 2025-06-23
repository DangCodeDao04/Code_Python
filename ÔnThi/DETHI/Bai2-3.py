n = int(input("Nhập số nguyên từ (0<n<100) là:"))
while n<=0 or n>=100:
    print("Giá trị không hợp lệ.Vui lòng nhập lại")
    n = int(input("Nhập số nguyên (0<n<100) là:"))
day_so = []
for i in range(n):
    x = int(input(f"Nhập phần tử thứ {i+1} là:"))
    day_so.append(x)


tong = 0
dem = 0
for num in day_so:
    if num % 2 !=0:
        tong += num
        dem += 1
if dem > 0:
    tbc = tong/dem
    print("Trung binh cộng của phần tử là số lẻ:",{tbc})
    
else:
    print("Không phải phần tử lẻ")