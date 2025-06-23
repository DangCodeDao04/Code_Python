n = int(input("Nhập số lượng phần tử (0<n<100):"))
while n <=0 or n>=100:
    print("Giá trị không hợp lê.Vui lòng nhập lại.")
    n=int(input("Nhập só lượng phần tử (0<n<100):"))
day_so = []
for i in range(n):
    x = int(input(f"Nhập phần tử thứ {i+1}:"))
    day_so.append(x)
#In ra các số lẻ trong dãy
for m in day_so:
    if m % 2 != 0:
        print(m,end = ' ')
print() #dòng mới
day_sach_xoa = []
for m in day_so:
    if m % 2 == 0:
        day_sach_xoa.append(m)
print("Dãy sau khi xóa các số lẻ là:",day_sach_xoa)