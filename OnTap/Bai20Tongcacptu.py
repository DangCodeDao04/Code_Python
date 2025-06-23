n = int(input("Nhập các số nguyên:"))
while n>=0 or n <=100:
    n = int(input("Vui lòng nhập lại n trong khoảng (0<n<100):"))
day_so = []
for i in range(n):
    x =int(input(f"Nhập số phần tử thứ {i+1}:"))
    day_so.append(x)
tong_chan = sum(x for x in day_so if x % 2 == 0)
max_ptu = max(day_so)

print("Tổng các phần tử là số chẵn",{tong_chan})
print("Phần tử lớn nhất của dãy là:",{max_ptu})