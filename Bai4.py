import numpy as np
import matplotlib.pyplot as plt
  
  #tao dữ liệu
x = np.linspace(0,  1/2* np.pi , 100)
y = np.tan(x)

#ve đồ thị
plt.plot(x,y , label = "y = sin(x)", color = "blue")

plt.xlim(0, 2 * np.pi)
plt.ylim(-10, 10)

# d) Đặt tiêu đề và nhãn trục
plt.title("Đồ thị hàm Cosine")  
plt.xlabel("Góc (radian)")
plt.ylabel("Giá trị Cosine")  

# Thêm lưới và chú thích
plt.grid(True)
plt.axhline(0,color = "r", linewidth = 0.5)

# Hiển thị đồ thị
plt.show()