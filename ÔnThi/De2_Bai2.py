n = int(input("Nhập số phần tử 0<n<100"))
while n<=0 or n>=100:
    n = int(input("Vui lòng nhập lại phần tử."))
day_so = []
for i in range(n):
    x = int(input(f"Nhập phần tử thứ {i+1} là:"))
    day_so.append(x)
    
tong_so_chan = 0
for m in day_so:
    if m % 2 == 0:
        tong_so_chan += m
print("\n Danh sách tổng phần tử số chẵn",tong_so_chan)
max_ptu = max(day_so)
print("\n Danh sách lớn nhất của dãy số là:",max_ptu)

