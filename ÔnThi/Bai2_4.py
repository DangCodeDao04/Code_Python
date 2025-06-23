n = int(input("Nhập số lượng phần tử (0<n<100):"))
while n<=0 or n>=100:
    print("Giá trị không hợp lệ.Vui lòng nhập lại.")
    n = int(input("Nhập số lượng phần tử (0<n<100):"))
day_so= []
for i in range(n):
    x = int(input(f"Nhập phần tử thứ {i+1}:"))
    day_so.append(x)
#Đếm số trong dãy bao nhiêu số dương
dem_so_duong = 0
for m in day_so:
    if m > 0:
        dem_so_duong += 1
        print("Số lượng số dương",{dem_so_duong})
        #Tìm số dương lớn nhất trong dãy 
min_so_duong = min(day_so)
print("Số dương nhỏ nhất của trong dãy là:",{min_so_duong})
