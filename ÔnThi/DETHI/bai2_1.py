n =int(input("Nhập số phần tử từ (0<n<100) là:"))
while n<=0 or n>=100:
    print("Giá trị không hợp lệ.Vui lòng nhập lại!")
    n = int(input("Nhập số phần tử từ (0<n<100) là:"))
#Nhập dữ liệu    
day_so = []
for i in range(n):
    x = int(input(f"Nhập số phần tử thứ {i+1} là:"))
    day_so.append(x)

#tính tổng các phần tử là số lẻ
tong_so_le = 0
for m in day_so:
    if m % 2 != 0:
        tong_so_le += m
print("\n Tổng các phần tử là số lẻ là:",tong_so_le)
min_ptu = min(day_so)
print("\n Phần tử nhỏ nhất của dãy là:",min_ptu)
   
