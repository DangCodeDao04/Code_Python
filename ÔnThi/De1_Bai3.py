class MatHang:
    def __init__(self,ma_hang = "",ten_hang = "",don_gia=0.0):
        self.ma_hang = ma_hang
        self.ten_hang = ten_hang
        self.don_gia = don_gia
    def __del__(self):
        pass
    def nhap(self):
        self.ma_hang = input("Nhập mã hàng của sản phẩm:")
        self.ten_hang = input("Nhập tên hãng sản xuất của sản phẩm:")
        self.don_gia = input("Nhập đơn giá của sản phẩm:")
    def xuat(self):
        print("Mã hàng:",self.ma_hang)
        print("Tên hãng sản xuất:",self.ten_hang)
        print("Đơn giá:",self.don_gia)

ds_mat_hang = []
n =int(input("Nhập số lương mặt hàng là:"))
for i in range(n):
    print(f"Nhập thông tin mặt hàng thứ {i+1}")
    mh = MatHang()
    mh.nhap()
    ds_mat_hang.append(mh)

#Hiện thị danh sách 
print("\n Danh sách mặt hàng ") 
for mh in ds_mat_hang:
    mh.xuat()
#Hiện thị danh sách giảm dần của đơn giá 
ds_mat_hang.sort(key = lambda mh : mh.don_gia,reverse = True)
print("\n Danh sách sau khi sắp xếp giảm dần của đơn giá:")
for mh in ds_mat_hang:
    mh.xuat()

#Xóa vị trí k 
k = int(input("Nhập vị trí cần xóa sản phẩm từ (0<n<100):"))
if 0 <= k < len(ds_mat_hang):
    del ds_mat_hang[k]
    print("\n Danh sách sau khi xóa khỏi danh sách")
    for mh in ds_mat_hang:
        mh.xuat()