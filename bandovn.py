import geopandas as gpd
import matplotlib.pyplot as plt

# Tải bản đồ thế giới từ GeoPandas
world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

# Lọc dữ liệu của Việt Nam
vietnam = world[world.name == "Vietnam"]

# Thiết lập figure
fig, ax = plt.subplots(figsize=(8, 10))

# Vẽ bản đồ Việt Nam với kiểu bút chì (không tô màu nền)
vietnam.boundary.plot(ax=ax, color='red', linewidth=1.5)

# Tùy chỉnh giao diện giống tranh vẽ bằng bút chì
ax.set_title('Bản đồ Việt Nam - Vẽ kiểu bút chì viền đỏ', fontsize=14, fontweight='bold')
ax.set_facecolor('white')
ax.axis('off')

# Hiển thị
plt.show()
