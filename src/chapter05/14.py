import numpy as np
import matplotlib.pyplot as plt

# 模拟迭代次数
iterations = 1000

# 生成随机梯度下降的损失曲线 (更大的波动)
sgd_loss = np.random.normal(loc=0.5, scale=0.2, size=iterations) + np.linspace(1, 0.1, iterations)

# 生成小批量梯度下降的损失曲线 (较小的波动)
mini_batch_loss = np.random.normal(loc=0.5, scale=0.05, size=iterations) + np.linspace(1, 0.1, iterations)

# 创建图表
plt.figure(figsize=(12, 6))
plt.plot(sgd_loss, label='随机梯度下降 (SGD)', alpha=0.7)
plt.plot(mini_batch_loss, label='小批量梯度下降 (Mini-batch GD)', alpha=0.7)

plt.title('随机梯度下降 vs 小批量梯度下降的损失函数波动对比')
plt.xlabel('迭代次数')
plt.ylabel('损失')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.7)

plt.show()