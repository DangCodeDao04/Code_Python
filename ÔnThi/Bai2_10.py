n = int(input("Nhập số lượng phần tử (0<n<100):"))
while n<=0 or n>=100:
    print("Giá trị không hợp lệ .Vui lòng nhập lại.")
    n = int(input("Nhập số lượng phần tử (0<n<100):"))
day_so = []
for i in range(n):
    x = int(input(f"Nhập số phần tử thứ {i+1} là:"))
    day_so.append(x)

def tim_vi_tri_x(day_so,x):
    vi_tri = []
    for i in range(len(day_so)):
        if day_so[i] == x:
            vi_tri.append(i)
    if len(vi_tri) == 0:
        print(f"Số {x} không xuất hiện trong dãy.")
    else:
        print(f"Số {x} xuất hiện trong dãy tại các vị trí: {vi_tri}")
def xoa_va_in_lai(day_so,x):
    day_moi = []
    for a in day_so:
        if a != x:
            day_moi.append(a)
    print("Dãy sau khi xóa các số bảng x:")
    for a in day_moi:
        print(a,end = ' ')
    print()

x = int(input("Nhập số x:"))
tim_vi_tri_x(day_so,x)
xoa_va_in_lai(day_so,x)