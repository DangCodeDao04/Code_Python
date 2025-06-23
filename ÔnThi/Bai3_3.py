class NhanVien:
    def __init__(self,ma_nv = "",ho_ten = "",chuc_vu = "",luong=0.0):
        self.ma_nv = ma_nv
        self.ho_ten = ho_ten
        self.chuc_vu = chuc_vu
        self.luong = luong
    def __del__(self):
        pass
#Hàm nhập dữ liệu cho một đôi tượng
def nhap(self):
    self.ma_nv = input("Nhập mã nhân viên:")
    self.ho_ten = input("Nhập họ tên:")
    self.chuc_vu = input("Nhập chức vụ:")
    self.luong = input("Nhập lương cơ bản:")
    
#Hàm xuất dữ liệu cho dối tượng
def xuat(self):
    print(f"Mã nhân viên:",self.ma_nv)
    print(f"Họ tên:",self.ho_ten)
    print(f"Chức vụ:",self.chuc_vu)
    print(f"Lương cơ bản:",self.luong)

#Khai báo và nhập dữ liệu
ds_nhan_vien = []
n = int(input("Nhập số lượng nhân viên:"))
for i in ds_nhan_vien:
    print(f"Nhập thông tin nhân viên thứ {i+1} là:")
    nv = NhanVien()
    nv.nhap()
    ds_nhan_vien.append(nv)

#Hiển thị thông tin
print("\n Danh sách nhân viên:") 
for nv in ds_nhan_vien:
          nv.xuat()

#Sắp xếp theo thứ tự tăng dần 
ds_nhan_vien.sort(key = lambda nv : nv.ma_nv)
for nv in ds_nhan_vien:
    nv.xuat()

#Thêm vị trí k
k = int(input("Nhập vị trí cần thêm nhân viên (bắt đầu từ 0) là:"))
if 0 <= k <= len(ds_nhan_vien):
    print("Nhập thông tin nhân viên mới:")
    nv_moi = NhanVien()
    nv_moi.nhap()
    ds_nhan_vien.insert(k,nv_moi)
    print("\n Danh sách nhân viên sau khi thêm:")
    for nv in ds_nhan_vien:
        nv.xuat()
else:
    print("Vị trí không hợp lệ.")

#Xóa vị trí k
k = int(input("Nhập vị trí cần xóa nhân viên (bắt đầu từ 0) là:"))
if 0  <= k < len(ds_nhan_vien):
    del ds_nhan_vien[k]
    print("\n Danh sách nhân viên sau khi xóa:")
    for nv in ds_nhan_vien:
        nv.xuat()
else:
    print("Vị trí không hợp lệ.")
