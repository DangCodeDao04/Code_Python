class HangHoa:
    def __init__(self,mahang = "",tenhang = "",dongia =0.0):
        self.mahang = mahang
        self.tenhang = tenhang
        self.dongia = dongia
    def __del__(self):
        pass   
    def nhap(self):
        self.mahang = input("Nhập mã hàng:")
        self.tenhang = input("Nhập tên hàng: ")
        self.dongia = input("Nhập đơn giá:")
    def xuat(self):
        print(f"Mã Hàng:", {self.mahang})
        print(f"Tên Hàng",{self.tenhang} )
        print(f"Đơn giá:",{self.dongia})
#b, Nhập danh sách n mặt hàng
ds = []
n = int(input("Nhập số lượng hàng hóa(nnn):"))
for i in range(n):
    print(f"Nhập mặt hàng thứ{i+1}:")
    mh = HangHoa()
    ds.append(mh)
    print("\nHiển thị mặt hàng:")
for i in ds:
    i.xuat()
#c,Hiện thị danh sách mặt hàng theo thứ tự 
ds.sort(key = lambda x : x.dongia)
print("\n Danh sách mặt hàng theo đơn giá tăng dần: ")
for mh in ds:
    mh.xuat()
#xóa khỏi danh sách 
k = int(input("\nNhập vị trí k cần xóa (bắt đầu từ 0): "))

if 0 <= k < len(ds):
    del ds[k]
    print(f"\nĐã xóa mặt hàng tại vị trí {k}. Danh sách còn lại:")
    for mh in ds:
        mh.xuat()
else:
    print("Vị trí không hợp lệ.")
        