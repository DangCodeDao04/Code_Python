n = int(input("Nhập số lương phần tử (0<n<100):"))
while n<=0 or n>=100:
    print(("Nhập phần tử không hợp lệ.Vui lòng nhập lại."))
    n = int(input("Nhập số lượng phần tử (0<n<100) là:"))
    
day_so = []
for i in range(n):
    x = int(input(f"Nhập phần tử thứ {i+1}:"))
    day_so.append(x)
    
tong_phan_le = 0
for m in day_so:
    if m  % 2 != 0:
        tong_phan_le += m
print("\n Tổng các phần tử là số lẻ:",tong_phan_le)
min_ptu = min(day_so)
print("\n Phần tử nhỏ nhất của dãy là:",min_ptu)