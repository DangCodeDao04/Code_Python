import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,2 * np.pi,100)

y_sin =np.sin(x)
y_cos = np.cos(x)

plt.plot(x,y_sin,label = 'y = sin(x)',color = 'blue')
plt.plot(x,y_cos,label = 'y = cos(x)',color = 'red')
plt.title("Đồ thị của hàm sin và cos")
plt.legend()
plt.grid(True)
plt.show()
