import numpy as np
import matplotlib.pyplot as plt

#vẽ đồ thị hàm y = sin(x) trên đoạn [0;2pi]
x = np.linspace(0,2 *np.pi,100)
y = np.sin(x)

plt.plot(x,y,label = 'y = sin(x)',color = 'blue')
plt.title("Đồ thị hàm Cosine")

plt.xlim(0,2 *np.pi)
plt.ylim(-1,1)

plt.xlabel("Góc (radian)")
plt.ylabel("Giá trị Cosine")

plt.legend()
plt.grid(True)
plt.show()
