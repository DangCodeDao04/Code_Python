import numpy as np
import matplotlib.pyplot as plt

# Tạo mảng x, tránh các điểm tiệm cận của tan(x) và cot(x)
x = np.linspace(0.01, np.pi - 0.01, 100)  # tránh x=0 và x=pi để không chia cho 0
x2 = np.linspace(0.01, np.pi - 0.01, 100)  #100 : số lượng phần tử được tạo ra 

# Tính giá trị tan(x) và cot(x)
y_tan = np.tan(x)
y_cot = 1/np.tan(x2)  # cot(x) = 1/tan(x)

# Vẽ đồ thị
plt.plot(x, y_tan, label='y = tan(x)', color='blue')
plt.plot(x2, y_cot, label='y = cot(x)', color='red')

# Vẽ tiệm cận đứng tại x = pi/2
plt.axvline(np.pi/2, color='black', linestyle='--', label='x = π/2')

# Giới hạn trục tung để đồ thị dễ nhìn hơn
plt.ylim(-10,10)

# Thêm tiêu đề và nhãn trục
plt.title('Đồ thị của hàm tan và cot')
plt.xlabel('Góc (radian)')
plt.ylabel('Giá trị hàm số')

# Thêm lưới và chú thích
plt.grid(True)
plt.legend()
plt.show()
