n = int(input("Nhập số lượng phần tử trong (0<n<100) là: "))
while n<=0 or n>=100:
    print("Giá trị không hợp lệ.Vui lòng nhập lại!")
    n = int(input("Nhập số lượng phần tử (0<n<100) là:"))
day_so = []
for i in range(n):
    x = int(input(f"Nhập phần tử thứ {i+1} là:"))
    day_so.append(x)

so_le = 0
for num in day_so:
    if num % 2 != 0:
        print(num,end = '')
print()

danh_sach_xoa = []
for num in day_so:
    if num % 2 == 0:
        danh_sach_xoa.append(num)
print("\n Danh sách sau khi xóa:",danh_sach_xoa)
