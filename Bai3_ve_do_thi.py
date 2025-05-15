import numpy as np
import matplotlib.pyplot as plt

def draw_branch(x, y, angle, length, depth, ax):
    if depth == 0:
        return
    
    # Tính toán điểm cuối của nhánh
    x_end = x + length * np.cos(angle)
    y_end = y + length * np.sin(angle)
    
    # Vẽ nhánh
    ax.plot([x, x_end], [y, y_end], 'k', linewidth=depth)
    
    # Giảm chiều dài nhánh và gọi đệ quy
    new_length = length * 0.7
    new_depth = depth - 1

    # Góc lệch trái/phải
    angle_variation = np.pi / 6  

    draw_branch(x_end, y_end, angle - angle_variation, new_length, new_depth, ax)
    draw_branch(x_end, y_end, angle + angle_variation, new_length, new_depth, ax)

# Khởi tạo đồ thị
fig, ax = plt.subplots(figsize=(6, 8))
ax.set_xlim(-1, 1)
ax.set_ylim(0, 2)
ax.axis('off')

# Vẽ cây
draw_branch(0, 0, np.pi/2, 1, 10, ax)

plt.show()
