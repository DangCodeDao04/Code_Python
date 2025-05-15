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
        print(f"Mã hàng: {self.ma_hang} | Tên hàng: {self.ten_hang} | Đơn giá: {self.don_gia:,.0f}")

# Sử dụng lớp HangHoa
if __name__ == "__main__":
    # Tạo danh sách hàng hóa
    ds_hang = []
    n = int(input("Nhập số lượng hàng hóa: "))
    
    # Nhập thông tin hàng hóa
    for i in range(n):
        print(f"\nNhập thông tin hàng hóa thứ {i+1}:")
        hang = HangHoa()
        hang.nhap()
        ds_hang.append(hang)
    
    # Hiển thị danh sách hàng hóa
    print("\nDanh sách hàng hóa:")
    print("{:<10} {:<20} {:<10}".format("Mã hàng", "Tên hàng", "Đơn giá"))
    print("-" * 40)
    for hang in ds_hang:
        hang.xuat()
        
 