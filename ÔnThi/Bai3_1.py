class SinhVien:
    def __init__(self,ma_sv = "",ho_ten= "",nganh_hoc= "",diem_tb = 0.0):
       self.ma_sv = ma_sv
       self.ho_ten = ho_ten
       self.nganh_hoc = nganh_hoc
       self.diem_tb = diem_tb
# Hàm nhập dữ liệu cho một đối tượng. 
    def nhap(self):
        self.ma_sv = input("Nhập mã sinh viên:")
        self.ho_ten = input("Nhập họ tên:")
        self.nganh_hoc = input("Nhập ngành học:")
        self.diem_tb = input(("Nhập điểm trung bình:"))
# Hàm xuất dữ liệu của một đối tượng.  
    def xuat(self):
        print(f"Mã sinh viên:",self.ma_sv)
        print(f"Họ tên:",self.ho_ten)
        print(f"Ngành học:",self.nganh_hoc)
        print(f"Điểm trung bình:",self.diem_tb)
#Khai báo và nhập danh sách 
ds_sinh_vien = []
n = int(input("Nhập số lượng sinh viên:"))
for i in range(n):
    print(f"Nhập thông tin sinh viên thứ {i+1} là:")
    sv = SinhVien()
    sv.nhap()
    ds_sinh_vien.append(sv)
#Hiện thị thông tin
print("\n Danh sách sinh viên:")
for sv in ds_sinh_vien:
    sv.xuat()
#Sắp xếp các đối tượng theo thứ tự tăng dần 
ds_sinh_vien.sort(key = lambda sv: sv.ma_sv)
print("\n Danh sách  sinh viên sau khi sắp xếp theo mã sinh viên là:")
for sv in ds_sinh_vien:
    sv.xuat()
    
#Thêm 1 sinh viên vào vị trí k
k = int(input("\n Nhập vị trí cần thêm sinh viên (bắt đầu từ 0) là:"))
if 0 <= k <= len(ds_sinh_vien):
    print("Nhập thông tin sinh viên mới:")
    sv_moi = SinhVien()
    sv_moi.nhap()
    ds_sinh_vien.insert(k,sv_moi)
    print("\n Danh sách sinh viên sau khi thêm:")
    for sv in ds_sinh_vien:
        sv.xuat()
else:
    print("Vị trí không hợp lệ.")
    
    
#Xóa sinh viên tại vị trí k
k = int(input("Nhập ví trí cần xóa sinh viên (bắt đầu từ 0) là:"))
if 0 <=k < len(ds_sinh_vien):
    del ds_sinh_vien[k]
    print("\n Danh sách sinh viên sau khi xóa:")
    for sv in ds_sinh_vien:
        sv.xuat()
else:
    print("Vị trí không hợp lệ.")