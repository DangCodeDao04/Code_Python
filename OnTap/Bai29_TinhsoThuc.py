n = int(input("Nhập số thực n:"))
while n>=0 or n<= 100:
    n =int(input("Vui long nhap lai so thuc tu(0<n<100):"))
    day_so = []
    for i in range(n):
        x = int(input(f"Nhập phần tử thứ {i+1}:"))
        day_so.append(x)
ds_le = (x for x in day_so if x % 2 == 1)
tong = sum(ds_le)
soluong = len(ds_le)
tbc = tong/soluong

min_ptu = min(day_so)

print("TBC của số lẻ",{tbc})
print(f"Phần tử min:",{min_ptu})