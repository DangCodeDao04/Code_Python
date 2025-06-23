class MatHang:
 def __init__(self, mahang="", tenhang="", dongia=0.0):
        self.mahang = mahang
        self.ten_hang = tenhang
        self.don_gia = dongia
 
   
def __del__(self):
    pass
def nhap(self):
    self.mahang = input("Nhập ma hàng:")
    self.tenhang = input("Nhập tên hàng:")
    self.dongia = input("Nhập đơn giá:")
def xuat(self):
    print("Mã Hàng:",{self.mahang})
    print("Tên hàng:",{self.tenhang})
    print("Đơn giá:",{self.dongia})
ds = []
n = int(input("Nhập số lương mặt hàng(nnn):"))
for i in range(n):
     print(f"Nhập phần tử thứ {i+1}:")
     mh =MatHang()
     ds.append(mh)
        
for mh in ds:
    mh.xuat()
    