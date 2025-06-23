class DienThoai:
    def __init__(self, ma_dt="", ten_dt="", hang_sx="", gia=0.0):
        self.ma_dt = ma_dt
        self.ten_dt = ten_dt
        self.hang_sx = hang_sx
        self.gia = gia

    def __del__(self):
        # Hàm hủy - có thể thêm thông báo nếu cần
        pass

    def nhap(self):
        self.ma_dt = input("Nhập mã điện thoại: ")
        self.ten_dt = input("Nhập tên điện thoại: ")
        self.hang_sx = input("Nhập hãng sản xuất: ")
        self.gia = float(input("Nhập giá: "))

    def xuat(self):
        print(f"Mã: {self.ma_dt}, Tên: {self.ten_dt}, Hãng: {self.hang_sx}, Giá: {self.gia:.2f}")
# Nhập số lượng điện thoại
n = int(input("Nhập số lượng điện thoại (n): "))
danh_sach = []

for i in range(n):
    print(f"\nNhập thông tin điện thoại thứ {i+1}:")
    dt = DienThoai()
    dt.nhap()
    danh_sach.append(dt)
print("\nDanh sách điện thoại vừa nhập:")
for dt in danh_sach:
    dt.xuat()
danh_sach.sort(key=lambda x: x.ma_dt)

print("\nDanh sách sau khi sắp xếp theo mã điện thoại:")
for dt in danh_sach:
    dt.xuat()
    
k = int(input("\nNhập vị trí cần chèn đối tượng mới (k): "))
if 1 <= k <= len(danh_sach)+1:
    dt_moi = DienThoai()
    print("Nhập thông tin điện thoại mới:")
    dt_moi.nhap()
    danh_sach.insert(k - 1, dt_moi)

    print("\nDanh sách sau khi chèn:")
    for dt in danh_sach:
        dt.xuat()
else:
    print("Vị trí không hợp lệ.")
    
k = int(input("\nNhập vị trí cần xóa đối tượng (k): "))
if 1 <= k <= len(danh_sach):
    del danh_sach[k - 1]

    print("\nDanh sách sau khi xóa:")
    for dt in danh_sach:
        dt.xuat()
else:
    print("Vị trí không hợp lệ.")
