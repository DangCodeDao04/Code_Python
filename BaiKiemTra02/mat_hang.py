class MatHang:
    def __init__(self, ma = " ", ten= " ", don_gia=0.0):
        self.ma = ma
        self.ten = ten
        self.don_gia = don_gia
    def __del__(self):
        print(f"Đã hủy mặt hàng: {self.ten}")
    
    def nhap(self):
        self.ma = input("Nhập mã mặt hàng: ")
        self.ten = input("Nhập tên mặt hàng: ")
        self.don_gia = float(input("Nhập đơn giá: "))
    
    def xuat(self):
        print(f"Mã: {self.ma} - Tên: {self.ten} - Đơn giá: {self.don_gia}")

ds_hang = []
n = int(input("Nhập số lượng mặt hàng: "))
for i in range(n):
    hang = MatHang()
    hang.nhap()
    ds_hang.append(hang)

print("Danh sách mặt hàng:")
for hang in ds_hang:
    hang.xuat()
    
ds_hang.sort(key=lambda x: x.don_gia, reverse=True)
print("Danh sách mặt hàng sau khi sắp xếp:")
for hang in ds_hang:
    hang.xuat()
ds_hang.remove(ds_hang[0])
print("Danh sách mặt hàng sau khi xóa:")
for hang in ds_hang:
    hang.xuat()