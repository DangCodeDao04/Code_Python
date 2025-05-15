n = int(input("Nhập số lượng phần tử( 0<n<100):"))
while n <=0 or n>=100:
    n = int(input("Nhập lại số lượng phần tử hợp lệ (0 < n < 100):"))

#nhap day so nguyen
day_so = []
for i in range(n):
    so = int(input(f"Nhập phần tử thứ {i + 1}:"))
    day_so.append(so)

#a Tính tổng các phần tử chẵn
tong_chan = 0
for x in day_so:
    if (x % 2) == 0:
        tong_chan += x

#tim phần tử lớn nhất
lon_nhat = max(day_so)
print("Tổng các phần tử chẵn là:", tong_chan)
print("Phần tử lớn nhất trong dãy là:", lon_nhat)
