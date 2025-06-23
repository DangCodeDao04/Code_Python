class Sach:
    def __init__(self,ma_sach = "",ten_sach = "",tac_gia = "",gia_ban =0.0):
        self.ma_sach = ma_sach
        self.ten_sach = ten_sach
        self.tac_gia = tac_gia
        self.gia_ban = gia_ban
#Hàm nhập dữ liệu cho một đối tượng.
    def nhap(self):
        self.ma_sach = input("Nhập mã sach:")
        self.ten_sach = input("Nhập tên sách:")
        self.tac_gia = input("Nhập tên tác giả:")
        self.gia_ban = input("Nhập giá bán:")
#Hàm xuất dữ liệu cho dối tượng
    def xuat(self):
        print(f"Mã sách:",self.ma_sach)
        print(f"Tên sách:",self.ten_sach)
        print(f"Tác giả:",self.tac_gia)
        print(f"Giá bán:",self.gia_ban)

#Khai báo và nhập dữ liệu 
ds_sach = []
n = int(input("Nhập số lượng sách:"))
for i in range(n):
    print(f"Nhập thông tin sách thứ {i+1} là:")
    sach = Sach()
    sach.nhap()
    ds_sach.append(sach)

#Hiện thị thổng tin sách
print("\n Danh sách  sách:")
for sach in ds_sach:
    sach.xuat()
    
#Sắp xếp theo thứ tự tăng dần
ds_sach.sort(key = lambda sach: sach.ma_sach)
print("\n Danh sách sách sau khi sắp xếp  tăng dần theo mã sách:")
for sach in ds_sach:
    sach.xuat()
    
#Them vào vị trí thứ k
k =int(input("Nhập vị trí cần thêm sách (bắt đầu từ 0) là:"))
if 0 <= k <=len(ds_sach):
    print("Nhập thông tin sách mới:")
    sach_moi = Sach()
    sach_moi.nhap()
    ds_sach.insert(k,sach_moi)
    print("\n Danh sách sách sau khi thêm:")
    for sach in ds_sach:
        sach.xuat()
else:
    print("Vị trí không hợp lệ.")
    
#Xóa vị trí thứ k 
k = int(input("Nhập vị trí cần xóa sách (bắt đầu từ 0) là:"))
if 0 <= k < len(ds_sach):
    del ds_sach[k]
    print("\n Danh sách sách sau khi xóa:")
    for sach in ds_sach:
        sach.xuat()
else:
    print("Vị trí không hợp lệ.")