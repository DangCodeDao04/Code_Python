import matplotlib.pyplot as plt

# Dữ liệu
nhom_tuoi = ['0-14', '15-24', '25-54', '55-64', '65+']
ty_le = [20, 15, 40, 10, 15]

# Vẽ biểu đồ tròn
plt.figure(figsize=(8, 6))
plt.pie(ty_le, labels=nhom_tuoi, autopct='%1.1f%%', startangle=90)

# Đảm bảo hình tròn chính xác
plt.axis('equal')

# Tiêu đề
plt.title("Phân phối dân số theo nhóm tuổi")

# Hiển thị biểu đồ
plt.show()
