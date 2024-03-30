# 3维向量
import numpy as np
import matplotlib.pyplot as plt

v = np.array([4, 1, 2])
print(v)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.quiver(0, 0, 0, v[0], v[1], v[2])
ax.set_xlim([0, 5])
ax.set_ylim([0, 5])
ax.set_zlim([0, 5])
plt.show()

