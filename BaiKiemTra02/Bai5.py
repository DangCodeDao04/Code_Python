import numpy as np
import matplotlib.pyplot as plt

#tao mang x, trach cac diem tiem can cua sin vs cosx
x = np.linspace(0,2 *np.pi,1000)
y = np.sin(x)

#Vẽ đồ thị 
plt.plot(x, y, color ='blue',label='y = cos(x)')
plt.title("Đồ thị hàm Cosine")
plt.xlabel("Góc radian")
plt.ylabel("Giá trị Cosine")
plt.xlim(0,2 * np.pi)
plt.ylim(-1,1)
plt.grid(True)
plt.legend()
plt.show()