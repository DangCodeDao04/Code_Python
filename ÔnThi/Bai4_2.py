import numpy as np
import matplotlib.pyplot as plt

#Tạo dữ liệu 
x = np.linspace(-np.pi/2 , np.pi/2 , 100)
y = np.tan(x)

#Vẽ đồ thị 
plt.plot(x,y,label = 'y = tan(x)',color = 'blue')
plt.title("Đồ thị hàm Tan")

#Thiết lập trục
plt.xlim(-np.pi/2,np.pi/2)
plt.ylim(-1,1)

#Đặt tiêu đề và nhãn 
plt.xlabel("Góc (radian)")
plt.ylabel("Giá trị Tan")

#Hiện thị chú thích
plt.legend()

#Hiện thị đồ thị
plt.grid(True)
plt.show()