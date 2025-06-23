class SanPham:
    def __init__(self,ma_sp = "",ten_sp = "",hang_sx = "",don_gia = 0.0):
        self.ma_sp = ma_sp
        self.ten_sp = ten_sp
        self.hang_sx = hang_sx
        self.don_gia = don_gia
    def __del__(self):
        pass 
    def nhap(self):
        self.ma_sp = input("Nhập mã sản phẩm:")
        self.ten_sp = input("Nhập tên sản phẩm:")
        self.hang_sx = input("Nhập hãng sản xuất:")
        self.don_gia = input("Nhập đơn giá:")
    def xuat(self):
        print(f"Mã sản phẩm:",self.ma_sp)
        print(f"Tên sản phẩm:",self.ten_sp)
        print(f"Hãng sản xuất:",self.hang_sx)
        print(f"Đơn giá:",self.don_gia)
    #Khai báo và nhập dữ liệu 
ds_san_pham = []
n = int(input("Nhập số lượng sản phẩm:"))
for i in range(n):
        print(f"Nhập thông tin sản phẩm thứ {i+1} là:")
        sp = SanPham()
        sp.nhap()
        ds_san_pham.append(sp)
    
#Hiện thi thông tin
print(" \n Danh sách sản phẩm:")
for sp in ds_san_pham:
    sp.xuat()

#Sắp xếp theo thứ tự tăng dần 
ds_san_pham.sort(key = lambda sp :sp.ma)
print("\n Danh sách sau khi sắp xếp tăng dần theo mã sản phẩm:")
for sp in ds_san_pham:
    sp.xuat()

#Thêm vào vị trí thứ k
k = int(input("Nhập vào vị trí cần thêm sản phẩm (bắt đầu từ 0) là:"))
if 0 <= k <= len(ds_san_pham):
    print("Nhập thông tin sản phẩm mới:")
    sp_moi = SanPham()
    sp_moi.nhap()
    ds_san_pham.insert(k,sp_moi)
    print("\n Danh sách sản phẩm sau khi thêm:")
    for sp in ds_san_pham:
        sp.xuat()
else:
    print("Vị trí không hợp lệ.")

#Xóa vị trí thứ k
k = int(input("Nhập vào vị trí cần xóa sản phẩm (bắt đầu từ 0) là:"))
if 0 <= k < len(ds_san_pham):
    del ds_san_pham[k]
    print("\n Danh sách sản phẩm sau khi xóa:")
    for sp in ds_san_pham:
        sp.xuat()
else:
    print("Vị trí không hợp lệ.")