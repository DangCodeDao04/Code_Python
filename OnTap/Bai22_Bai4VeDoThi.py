import numpy as np
import matplotlib.pyplot as plt

#Vẽ đồ thị y= sin(x) trong khoảng (0,2pi)
x = np.linspace(0,2 *np.pi,100)
y = np.sin(x)

#Đặt tiêu đề cho biểu đồ "Đồ thị hàm Cosine"
plt.plot(x,y,label = 'y = sin(x)',color = 'blue')
plt.title("Đồ thị hàm Cosine")

#trục x hiện thị từ 0 đến 2pi trục y hiện thị từ -1 đến 1
plt.xlim(0,2 *np.pi)
plt.ylim(-1,1)
#Đặt nhãn trục x là "Góc (radian)"và trục y là "Giá trị cosine"
plt.xlabel("Góc(radian)")
plt.ylabel("Giá trị Cosine")

plt.legend()
plt.grid(True)
plt.show
