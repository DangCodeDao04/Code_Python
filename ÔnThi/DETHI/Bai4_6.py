import matplotlib.pyplot as plt

#tạo dữ liệu
thang = ['Tháng 1', 'Tháng 2', 'Tháng 3', 'Tháng 4', 'Tháng 5', 'Tháng 6',
         'Tháng 7', 'Tháng 8', 'Tháng 9', 'Tháng 10', 'Tháng 11', 'Tháng 12']
nhiet_do = [17, 18, 21, 26, 30, 32, 33, 32, 30, 27, 23, 19]

# 4_4_5.2: Vẽ biểu đồ hình cột
plt.figure(figsize=(10, 6))
plt.plot(thang, nhiet_do, marker='o', color='blue', linestyle='-')

# 4_4_5.3: Đặt tiêu đề biểu đồ
plt.title("Lượng mưa trung bình các tháng trong năm")

# 4_4_5.4: Đặt nhãn trục x và y
plt.xlabel("Tháng")
plt.ylabel("Lượng mưa (mm)")

# Hiển thị biểu đồ
plt.grid(True)
plt.tight_layout()
plt.show()
