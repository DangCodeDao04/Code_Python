class ChuyenBay:
    def __init__(self,so_hieu = "",diem_di = "",diem_den = ""):
        self.so_hieu = so_hieu
        self.diem_di = diem_di
        self.diem_den = diem_den
    def __del__(self):
        pass
    def nhap(self):
        self.so_hieu = input("Nhập số hiệu hãng bay:")
        self.diem_di = input("Nhập điểm đi:")
        self.diem_den = input("Nhập điểm đến:")
    def xuat(self):
        print("Số hiệu:",self.so_hieu)
        print("Diểm đi",self.diem_di)
        print("Diểm đến:",self.diem_den)
    
ds_chuyen_bay = []
n = int(input("Nhập số lượng chuyến bay:"))
for i in range(n):
    print(f"Nhập thông tin chuyên bay thứ {i+1}:")
    chuyen_bay =ChuyenBay()
    chuyen_bay.nhap()
    ds_chuyen_bay.append(chuyen_bay)
    

print("\n Danh sách chuyến bay")
for chuyen_bay in ds_chuyen_bay:
    chuyen_bay.xuat()
    
ds_chuyen_bay.sort(key = lambda chuyen_bay :chuyen_bay.so_hieu)
print("\Danh sách sau khi sắp xếp tăng dần theo số hiệu là:")
for chuyen_bay in ds_chuyen_bay:
    chuyen_bay.xuat()

k = int(input("Nhập vị trí cần thêm trong danh sách là:"))
if 0<= k <= len(ds_chuyen_bay):
    print("Nhập thông tin chuyen bay moi:")
    chuyen_bay_moi = ChuyenBay()
    chuyen_bay_moi.nhap()
    ds_chuyen_bay.insert(k,chuyen_bay_moi)
    print("\n Danh sách sau khi thêm là:")
    for chuyen_bay in ds_chuyen_bay:
        chuyen_bay.xuat()
else:
    print("Giá trị không hợp lệ")

k = int(input("Nhập vị trí cần xóa trong danh sách là:"))
if 0<=k < len(ds_chuyen_bay):
    del ds_chuyen_bay[k]
    print("Danh sách sau khi xóa là:")
    for chuyen_bay in ds_chuyen_bay:
        chuyen_bay.xuat()

    