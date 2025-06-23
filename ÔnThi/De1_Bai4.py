import numpy as np
import matplotlib.pyplot as plt

#Tạo dữ liệu
x = np.linspace(0, 2 *np.pi,100)
y = np.sin(x)

#Vẽ đồ thị 
plt.plot(x,y,label = 'y = sin(x)',color ='blue')
plt.title("Đồ thị hàm Cosine")

#Tiêu đề và nhãn
plt.xlabel("Góc (radian)")
plt.ylabel("Giá trị Cosine")

#Thiết lập trục
plt.xlim(0,2 * np.pi)
plt.ylim(-1,1)

#Hiện thị chú thích
plt.legend()
plt.axhline(y=0, color='black', linewidth=1)
#hiện đồ thị
plt.grid(True)
plt.show()