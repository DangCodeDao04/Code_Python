n =int(input("Nhập só lượng phần tử (0<n<100):"))
while n<=0 or n>=100:
    print("Vui lòng nhập lại số phần tử.")
    n = int(input("Nhập số lượng phần tử (0<n<100):"))
day_so = []
for i in range(n):
    x = int(input(f"Nhập số lượng phần tử thứ {i+1} là:"))
    day_so.append(x)
tong_so_chan = 0
for m in day_so:
    if m % 2 == 0:
     tong_so_chan += m
print("\ Tổng các phần tử là số chẵn:",tong_so_chan)
max_ptu = max(day_so)
print("Phần tử lớn nhất của dãy là:",max_ptu)
  
