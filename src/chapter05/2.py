import numpy as np
import matplotlib.pyplot as plt

# 生成训练数据
np.random.seed(0)
x_train = np.linspace(0, 10, 100)
y_train = 2 * x_train + 1 + np.random.normal(0, 2, 100)

# 训练线性回归模型
coefficients = np.polyfit(x_train, y_train, 1)
model = np.poly1d(coefficients)

# 生成测试数据（外推区域）
x_test = np.linspace(20, 30, 100)
y_test = 2 * x_test + 1 + np.random.normal(0, 2, 100)  # 使用相同的真实关系，但更大的x值

# 进行预测
y_pred_train = model(x_train)
y_pred_test = model(x_test)

# 绘制图形
plt.figure(figsize=(10, 6))
plt.scatter(x_train, y_train, color='blue', label='Training Data')
plt.plot(x_train, y_pred_train, 'g-', label='Model (Trained 0-10)')
plt.scatter(x_test, y_test, color='red', label='Test Data (20-30)')
plt.plot(x_test, y_pred_test, 'r-', label='Prediction (20-30)')
plt.xlabel('X Value')
plt.ylabel('Y Value')
plt.title('Visualization of Linear Regression Extrapolation')
plt.legend()
plt.grid(True)
plt.show()

# 可以发现：模型在红色的点上面的表现欠佳