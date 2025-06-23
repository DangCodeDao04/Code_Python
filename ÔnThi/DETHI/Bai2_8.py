n = int(input("Nhập số lượng phần tử (0<n<100):"))
while n<=0 or n>= 100:
    print("Giá trị không hợp lê.Vui lòng nhập lại.")
    n =int(input("Nhập số lượng phần tử (0<n<100) là:"))
day_so = []
for i in range(n):
    x = int(input(f"Nhập phần tử thứ {i+1} là:"))
    day_so.append(x)

so_duong =0
for m in day_so:
    if  m > 0:
        print(m,end = '')
print()
print("\n Danh sách các số chẵn trong dãy là:",so_duong)

ds_xoa = 0
for m in day_so:
    if x > 0:
        ds_xoa.append(m)
day_so.sort(reverse=True)
print("Danh sách sau khi xóa là:",ds_xoa)

