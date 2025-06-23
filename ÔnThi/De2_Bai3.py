class HangHoa:
    def __init__(self,ma_hang = "",ten_hang = "",don_gia = 0.0):
        self.ma_hang = ma_hang
        self.ten_hang = ten_hang
        self.don_gia = don_gia
    def __del__(self):
        pass
    def nhap(self):
        self.ma_hang = input("Nhập mã hàng:")
        self.ten_hang = input("Nhập tên hàng:")
        self.don_gia = input("Nhập đơn giá:")
    def xuat(self):
        print("Mã hàng:",self.ma_hang)
        print("Tên hàng:",self.ten_hang)
        print("Đơn giá:",self.don_gia)

ds_hang_hoa = []
n =int(input("Nhập số lượng hàng hóa:"))
for i in range(n):
    print(f"Nhập thông tin thứ {i+1} là:")
    hang_hoa = HangHoa()
    hang_hoa.nhap()
    ds_hang_hoa.append(hang_hoa)
    
#Hiện thị danh sách tăng dần 
ds_hang_hoa.sort(key = lambda hang_hoa:hang_hoa.don_gia)
print("\n Danh sách sau khi sắp xếp tăng dần theo đơn giá")
for hang_hoa in ds_hang_hoa:
    hang_hoa.xuat()

