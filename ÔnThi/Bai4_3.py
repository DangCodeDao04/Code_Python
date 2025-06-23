import numpy as np 
import matplotlib.pyplot as plt

#Tạo dữ liệu 
x = np.linspace(0, 2 * np.pi,100)
y = np.cos(x) ** 2

#Vẽ đồ thị 
plt.plot(x,y,label = 'y = cos^2(x)',color = 'blue')
plt.title("Đồ thị hàm cos^2(x)")

#Thiết lập trục
plt.xlim(0,2 * np.pi)
plt.ylim(0,1)

#Đặt tiêu đề và nhãn
plt.xlabel("Góc (radian)")
plt.ylabel("Giá trị y = cos^2(x)")

#Hiện thị chú thích
plt.legend()
#hiện thị đồ thị
plt.grid(True)
plt.show()
