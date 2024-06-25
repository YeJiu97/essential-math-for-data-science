import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 从给定的URL加载数据
data = pd.read_csv('https://bit.ly/2KF29Bd', header=0)

# 将数据集的第一列和第二列分别赋值给X和Y
X = data.iloc[:, 0].values
Y = data.iloc[:, 1].values
# 获取数据集的行数，即样本数
n = data.shape[0] 

# 初始化模型参数：斜率m和截距b
# 为两种梯度下降方法分别初始化
m_sgd = m_mbgd = 0.0
b_sgd = b_mbgd = 0.0

# 设置学习率
L = .0001 
# 设置梯度下降的迭代次数
epochs = 10000

# 用于存储每次迭代后的m和b值
m_sgd_values = []
b_sgd_values = []
m_mbgd_values = []
b_mbgd_values = []

# 执行梯度下降
for i in range(epochs):
    # 随机梯度下降, sample_size = 1
    idx = np.random.choice(n, 1, replace=False)
    x_sgd = X[idx]
    y_sgd = Y[idx]
    Y_pred_sgd = m_sgd * x_sgd + b_sgd
    D_m_sgd = (-2) * sum(x_sgd * (y_sgd - Y_pred_sgd))
    D_b_sgd = (-2) * sum(y_sgd - Y_pred_sgd)
    m_sgd -= L * D_m_sgd 
    b_sgd -= L * D_b_sgd
    m_sgd_values.append(m_sgd)
    b_sgd_values.append(b_sgd)
    
    # 小批量梯度下降, sample_size = 10
    idx = np.random.choice(n, 10, replace=False)
    x_mbgd = X[idx]
    y_mbgd = Y[idx]
    Y_pred_mbgd = m_mbgd * x_mbgd + b_mbgd
    D_m_mbgd = (-2 / 10) * sum(x_mbgd * (y_mbgd - Y_pred_mbgd))
    D_b_mbgd = (-2 / 10) * sum(y_mbgd - Y_pred_mbgd)
    m_mbgd -= L * D_m_mbgd
    b_mbgd -= L * D_b_mbgd
    m_mbgd_values.append(m_mbgd)
    b_mbgd_values.append(b_mbgd)

# 绘制m和b随迭代次数变化的图
plt.figure(figsize=(14, 6))

# 绘制m的变化
plt.subplot(1, 2, 1)
plt.plot(m_sgd_values, label='SGD m values', alpha=0.6)
plt.plot(m_mbgd_values, label='MBGD m values (batch size = 10)', alpha=0.6)
plt.title('Change of m over iterations')
plt.xlabel('Iterations')
plt.ylabel('m value')
plt.legend()

# 绘制b的变化
plt.subplot(1, 2, 2)
plt.plot(b_sgd_values, label='SGD b values', alpha=0.6)
plt.plot(b_mbgd_values, label='MBGD b values (batch size = 10)', alpha=0.6)
plt.title('Change of b over iterations')
plt.xlabel('Iterations')
plt.ylabel('b value')
plt.legend()

plt.tight_layout()
plt.show()