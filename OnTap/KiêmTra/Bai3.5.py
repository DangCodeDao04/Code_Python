class DienThoai:
    def __init__(self,ma= "",ten= "",hangsx= "",dongia = 0.0):
        self.ma = ma
        self.ten = ten
        self.hangsx = hangsx
        self.dongia = dongia
    def __del__(self):
        pass
    def nhap(self):
        self.ma = input("Nhập mã:")
        self.ten = input("Nhập ten:")
        self.hangsx = input("Nhập hangsx")
        self.dongia = input("Nhập don giá:")
    def xuat(self):
        print(f"Ma hang:",{self.ma})
        print(f"Tên hang",{self.ten})
        print(f"Hang sx:",{self.hangsx})
        print(f"Giá:",self.dongia)
n = int(input("Nhập số lượng n đối tượng:"))
dt = []
for i in range(n):
    print(f"Nhập sô lượng điện thoại thứ {i+1}:")
    mh = DienThoai()
    dt.append(mh)
    dt.sort(key = lambda x :x.ma)
for mh in dt:
    print(f"Danh sách sau khi nhập:")
    mh.xuat()
k = int(input("Nhập vị trị cần thêm của điện thoại:"))
if 1<=k<=len(dt)+1:
    ds_moi = DienThoai()
    print(f"Nhập điện thoại mới:")
    ds_moi.nhap()
    dt.insert(k-1,ds_moi)
else:
    print("Vui lòng nhập lại:")

k = int(input("Nhập vị trí cần xóa của k:"))
if 1 <= k<=len(dt):
    del dt[k-1]
    print("\n Danh sách sau khi xóa")
    for dt in range