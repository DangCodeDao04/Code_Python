import numpy as np
import matplotlib.pyplot as plt

#vẽ đồ thị hình sinx
x= np.linspace(0,2 * np.pi,100)
y=np.sin(x)

plt.plot(x,y,label ='y=sin(x)',color = 'red')
plt.title("Đồ thị hàm Cosine")
plt.legend()
plt.grid(True)
plt.show()
