import matplotlib.pyplot as plt

# Danh sách nhóm tuổi và tỉ lệ phần trăm tương ứng
labels = ['0-14', '15-24', '25-54', '55-64', '65+']
sizes = [20, 15, 40, 10, 15]

# Màu sắc tùy chọn (có thể bỏ qua để matplotlib tự chọn)
colors = ['#66b3ff', '#ff9999', '#99ff99', '#ffcc99', '#c2c2f0']

# Vẽ biểu đồ tròn
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, colors=colors)

# Đảm bảo biểu đồ là hình tròn chính xác
plt.axis('equal')

# Đặt tiêu đề cho biểu đồ
plt.title('Phân phối dân số theo nhóm tuổi')

# Hiển thị biểu đồ
plt.show()
