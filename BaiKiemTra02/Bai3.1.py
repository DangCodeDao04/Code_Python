class HangHoa:
    def __init__(self, ma_hang="", ten_hang="", don_gia=0.0):
        self.ma_hang = ma_hang
        self.ten_hang = ten_hang
        self.don_gia = don_gia

    def __del__(self):
        print(f"Đã hủy mặt hàng: {self.ten_hang}")

    def nhap(self):
        self.ma_hang = input("Nhập mã hàng: ")
        self.ten_hang = input("Nhập tên hàng: ")
        self.don_gia = float(input("Nhập đơn giá: "))

    def xuat(self):
        print("{:<10} {:<20} {:<10,.0f}".format(self.ma_hang, self.ten_hang, self.don_gia))

def hien_thi_tieu_de():
    print("\n{:<10} {:<20} {:<10}".format("Mã hàng", "Tên hàng", "Đơn giá"))
    print("-" * 40)

# b) Nhập danh sách
ds_hang = []
n = int(input("Nhập số lượng mặt hàng (n > 0): "))
for i in range(n):
    print(f"\nNhập mặt hàng thứ {i+1}:")
    hang = HangHoa()
    hang.nhap()
    ds_hang.append(hang)
ư
# c) Hiển thị danh sách sắp xếp theo đơn giá tăng dần
ds_hang.sort(key=lambda x: x.don_gia)
print("\n👉 Danh sách sau khi sắp xếp theo đơn giá tăng dần:")
hien_thi_tieu_de()
for hang in ds_hang:
    hang.xuat()

# d) Xóa phần tử tại vị trí k
k = int(input("\nNhập vị trí k muốn xóa (bắt đầu từ 1): "))
if 1 <= k <= len(ds_hang):
    del ds_hang[k - 1]
    print(f"\n Đã xóa mặt hàng ở vị trí {k}")
else:
    print(" Vị trí k không hợp lệ!")

# In lại danh sách sau khi xóa
print("\n Danh sách sau khi xóa:")
hien_thi_tieu_de()
for hang in ds_hang:    
    hang.xuat()
