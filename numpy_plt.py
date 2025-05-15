# vẽ hàm Sim từ 0->2pi
import numpy as np
x1= np.arange(0,2*np.pi, 2*np.pi/100.0  ) 
y1 = np.sin(x1)

x2 = np.linspace(0, 2*np.pi, 100)
y2= np.sin(x2+np.pi/4)

x3, i =[], 0
while i<2*np.pi:
    x3.append(i)
    i=i+ 0.2
x3= np.array(x3)
y3 = np.sin(x3+np.pi/2)
import matplotlib.pyplot as plt
plt.plot(x1, y1, "r")
plt.plot(x2, y2, "b")
plt.plot(x3, y3, "g")
plt.show()
