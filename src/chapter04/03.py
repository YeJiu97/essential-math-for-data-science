from numpy import array

v = array([3, 2])
w = array([2, -1])

# 相加
result = v + w

# 可视化向量 v 和 w
import matplotlib.pyplot as plt
plt.plot([0, v[0]], [0, v[1]], 'b', label='v')
plt.plot([0, w[0]], [0, w[1]], 'r', label='w')
plt.plot([0, result[0]], [0, result[1]], 'g', label='v+w')
plt.axis('equal')
plt.legend()
plt.show()