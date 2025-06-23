class MatHang:
  def __init__(self, mahang="", tenhang="", dongia=0.0):
        self.mahang = mahang
        self.tenhang = tenhang
        self.dongia = dongia
    def __del__(self):
        # Hàm hủy (không bắt buộc làm gì cụ thể trong Python)
        pass
    def nhap(self):
        self.mahang = input("Nhập mã hàng:")
        self.ten_hang = input("nhập tên hàng:")
        self.don_gia = input("Nhập đơn giá:")
    def xuat(self):
        print(f"Mã hàng:",{self.mahang})
        print(f"Hãng SX:",{self.ten_hang})
        print(f"Đơn giá:",{self.don_gia})
        
#Nhập danh sách n mặt hàng
n = int(input("Nhập số lượng mặt hàng (nnn):"))
ds =[]
for i in range(n):
    print(f"\n Nhập mặt hàng thứ {i+1}:")   
    mh = MatHang()
    mh.nhap()
    ds.append(mh)
    
ds_tablet = [mh for mh in ds if "máy tính bảng" in mh.ten_hang.lower()]
ds_tablet.sort(key=lambda x: x.don_gia, reverse=True)

for mh in ds_tablet:
    mh.xuat()

#Xóa mặt hàng tại ví trí k
k = int(input("\n Nhập vị trí cần xóa (tính từ 0): "))
if 0 <= k < len(ds):
    del ds[k]
    print("\nDanh sách mặt hàng sau khi xóa:")
    for mh in ds:
        mh.xuat()
else:
    print("Vị trí không hợp lệ.")
    