import matplotlib.pyplot as plt

# 4_3_5.1: Tạo danh sách các tháng và lượng mưa trung bình
thang = ['Tháng 1', 'Tháng 2', 'Tháng 3', 'Tháng 4', 'Tháng 5', 'Tháng 6',
         'Tháng 7', 'Tháng 8', 'Tháng 9', 'Tháng 10', 'Tháng 11', 'Tháng 12']
luong_mua = [30, 45, 60, 85, 100, 120, 150, 130, 110, 90, 50, 40]

# 4_4_5.2: Vẽ biểu đồ hình cột
plt.figure(figsize=(10, 6))
plt.bar(thang, luong_mua, color='mediumseagreen')

# 4_4_5.3: Đặt tiêu đề biểu đồ
plt.title("Lượng mưa trung bình các tháng trong năm")

# 4_4_5.4: Đặt nhãn trục x và y
plt.xlabel("Tháng")
plt.ylabel("Lượng mưa (mm)")

# Hiển thị biểu đồ
plt.show()
