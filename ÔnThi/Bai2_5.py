n =int(input("Nhập số lượng phần tử (0<n<100):"))
while n<=0 or n>=100:
    print("Giá trị không hợp lệ.Vui lòng nhập lại.")
    n = int(input(f"Nhập số phần tử (0<n<100) là:"))
day_so = []
for i in range(n):
    x =int(input(f"Nhập phần tử thứ {i+1} là:"))
    day_so.append(x)

dem_am = 0
for m in day_so:
    if m < 0:
        dem_am += 1
print("Số lượng số âm trong dãy là:",{dem_am})
max_am = max(day_so)
print("Số âm lớn nhất trong dãy là" ,{max_am})