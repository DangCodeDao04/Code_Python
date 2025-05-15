import numpy as np
import matplotlib.pyplot as plt
  #tao dữ liệu
x  = np.linspace(-np.pi/2 + 0.01, np.pi/2 - 0.01, 400)
y = np.tan(x)

#ve đồ thị
plt.plot(x,y , label = "y = tan", color = "blue")

plt.xlim(-np.pi/2,np.pi/2)
plt.ylim(-1, 1)

# d) Đặt tiêu đề và nhãn trục
plt.title("Đồ thị hàm Tan")  
plt.xlabel("Góc (radian)")
plt.ylabel("Giá trị Tanx")  

# Thêm lưới và chú thích
plt.grid(True)

# Hiển thị đồ thị
plt.show()