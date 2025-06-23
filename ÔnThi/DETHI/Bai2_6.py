n = int(input("Nhập số  lượng phần tử (0<n<100) là:"))
while n<=0 or n>=100:
    print("Giá trị không hợp lê.Vui lòng nhập lại ")
    n = int(input("Nhập số nguyên từ (0<n<100) là:"))
day_so = []
for i in range(n):
    x = int(input(f"Nhập phần tử thứ {i+1} là"))
    day_so.append(x)

#In ra các số chẵn 
so_chan = 0
for m in day_so:
    if m % 2 == 0:
        print(m,end ='')
print()
day_sach_xoa = []
for m in day_so:
    if m  != 0:
        day_sach_xoa.append(m)
print("\n Danh sách sau khi xóa là:",day_sach_xoa)

#Xóa các số 0 khỏi dãy 
