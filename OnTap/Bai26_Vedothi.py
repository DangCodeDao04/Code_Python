import numpy as np
import matplotlib.pyplot as plt

#Vẽ đồ thị hàm số y = tanx và y = cotx
x = np.linspace(0.01,np.pi - 0.01 , 1000)

#tính đồ thị 

y_tan = np.tan(x)
y_cot = 1/np.tan(x)

plt.plot(x,y_tan,label ="y = tãn(x)",color = "blue")
plt.plot(x,y_cot,label = "y = cot(x)",color = "red")
plt.title("Đồ thị hàm tan và cot")

plt.xlabel("Góc(radian)")
plt.ylabel("Giá trị hàm số")
plt.ylim(-10,10)
plt.legend()
plt.grid(True)
plt.show()