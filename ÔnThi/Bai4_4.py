import numpy as np
import matplotlib.pyplot as plt

#Tạo dữ liệu
x = np.linspace(0, np.pi,100)
y_tan = np.tan(x)
y_cot = 1/np.tan(x)

#vẽ đồ thị
plt.plot(x,y_tan,label = 'y = tan(x)',color = 'blue')
plt.plot(x,y_cot,label = 'y = cot(x)',color = 'red')
plt.title("Đồ thị của hàm tan và cot")

#Thiết lập trục
plt.xlim(0,np.pi)
plt.ylim(-10,10)

#Đặt tiêu đề và nhãn 
plt.xlabel("Góc (radian)")
plt.ylabel("Giá trị hàm số")

#Hiện thị chú thích
plt.legend()

#Hiện thị đồ thị 
plt.grid(True)
plt.show()
