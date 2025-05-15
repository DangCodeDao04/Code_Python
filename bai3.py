class MatHang:
    def __init__(self,ma_hang="",Ten_hang="",don_gia=0.0):
        self.ma_hang = ma_hang
        self.Ten_hang = Ten_hang
      
        self.don_gia = don_gia
    def __del__(self):
        pass
    def nhap(self):
        self.ma_hang = input("Nhập mã hàng: ")
        self.ten_hang = input("Nhập tên hãng sản xuất: ")
        self.don_gia = float(input("Nhập đơn giá: "))

    def xuat(self):
        print(f"Mã hàng: {self.ma_hang} | Hãng: {self.ten_hang} | Đơn giá: {self.don_gia:.2f}")    
    
nnn = int(input("Nhập số lượng mặt hàng: "))
danh_sach = []

for i in range(nnn):
    print(f"\nNhập mặt hàng thứ {i + 1}:")
    mh = MatHang()
    mh.nhap()
    danh_sach.append(mh)

# In sau khi đã nhập xong toàn bộ
print("\nHiển thị mặt hàng:")
for i in danh_sach:
    i.xuat()

danh_sach.sort(key=lambda x: x.don_gia, reverse=True)

print("\nDanh sách máy tính bảng (giảm dần theo đơn giá):")
for mh in danh_sach:
    mh.xuat()


k = int(input("\nNhập vị trí k cần xóa (bắt đầu từ 0): "))

if 0 <= k < len(danh_sach):
    del danh_sach[k]
    print(f"\nĐã xóa mặt hàng tại vị trí {k}. Danh sách còn lại:")
    for mh in danh_sach:
        mh.xuat()
else:
    print("Vị trí không hợp lệ.")


    