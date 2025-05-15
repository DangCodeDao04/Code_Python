import tkinter as tk         
from tkinter import nt    #dùng để báo hộp thoai lỗi

import math                  # Dùng để tính căn bậc hai (sqrt)

# Hàm xử lý khi bấm nút tính nghiệm
def giai_phuong_trinh():
    try:
        # Đọc dữ liệu nhập từ ô Entry và chuyển sang kiểu float
        a = float(entry_a.get())
        b = float(entry_b.get())
        c = float(entry_c.get())

        # Bắt đầu xử lý phương trình
        if a == 0:
            # Nếu a = 0 → phương trình bậc nhất bx + c = 0
            if b == 0:
                # Nếu cả a và b = 0
                if c == 0:
                    ket_qua = "Phương trình có vô số nghiệm"
                else:
                    ket_qua = "Phương trình vô nghiệm"
            else:
                x = -c / b
                ket_qua = f"Phương trình có nghiệm: x = {x:.2f}"
        else:
            # Trường hợp a khác 0 → phương trình bậc 2
            delta = b**2 - 4*a*c  # Tính biệt thức delta
            if delta < 0:
                ket_qua = "Phương trình vô nghiệm"
            elif delta == 0:
                x = -b / (2*a)
                ket_qua = f"Phương trình có nghiệm kép: x = {x:.2f}"
            else:
                x1 = (-b + math.sqrt(delta)) / (2*a)
                x2 = (-b - math.sqrt(delta)) / (2*a)
                ket_qua = f"Phương trình có 2 nghiệm:\nx1 = {x1:.2f}, x2 = {x2:.2f}"

        # Hiển thị kết quả lên label
        lbl_ket_qua.config(text=ket_qua)
    except:
        # Nếu nhập sai , hiện cảnh báo
       nt.showerror("Lỗi", "Vui lòng nhập số hợp lệ!")

# Tạo cửa sổ chính
window = tk.Tk()
window.title("Giải phương trình bậc 2")
window.geometry("400x250")  # Kích thước cửa sổ

# --- Giao diện nhập hệ số a, b, c ---
tk.Label(window, text="Hệ số a:").grid(row=0, column=0, padx=10, pady=5, sticky="e")
entry_a = tk.Entry(window)
entry_a.grid(row=0, column=1)

tk.Label(window, text="Hệ số b:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
entry_b =tk.Entry(window)
entry_b.grid(row=1, column=1)

tk.Label(window, text="Hệ số c:").grid(row=2, column=0, padx=10, pady=5, sticky="e")
entry_c = tk.Entry(window)
entry_c.grid(row=2, column=1)

# --- Nút tính ---
btn_tinh = tk.Button(window, text="Tính nghiệm", command=giai_phuong_trinh)
btn_tinh.grid(row=3, column=0, columnspan=2, pady=10)

# --- Label hiển thị kết quả ---
lbl_ket_qua = tk.Label(window, text="", fg="blue")
lbl_ket_qua.grid(row=4, column=0, columnspan=2)

# Chạy giao diện
window.mainloop()
