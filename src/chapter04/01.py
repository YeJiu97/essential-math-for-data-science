# 生成一个向量
v = [3, 2]  # 表示向量(3, 2)

# 使用numpy来表示向量
import numpy as np
v = np.array([3, 2])
print(v)

# 可视化向量 v
import matplotlib.pyplot as plt
plt.plot([0, v[0]], [0, v[1]])
plt.axis('equal')
plt.show()