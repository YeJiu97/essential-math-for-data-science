import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

# 加载数据
all_data = pd.read_csv("https://tinyurl.com/y2qmhfsr")
# 提取输入列，按255缩放
all_inputs = (all_data.iloc[:, 0:3].values / 255.0)
all_outputs = all_data.iloc[:, -1].values

# 分割训练和测试数据集
X_train, X_test, Y_train, Y_test = train_test_split(all_inputs, all_outputs, test_size=1/3)

# 初始化神经网络的权重和偏置
w_hidden = np.random.rand(3, 3)
w_output = np.random.rand(1, 3)
b_hidden = np.random.rand(3, 1)
b_output = np.random.rand(1, 1)

# 激活函数
relu = lambda x: np.maximum(0, x)
logistic = lambda x: 1 / (1 + np.exp(-x))

# 神经网络前向传播
def forward_prop(X):
    Z1 = w_hidden @ X + b_hidden
    A1 = relu(Z1)
    Z2 = w_output @ A1 + b_output
    A2 = logistic(Z2)
    return Z1, A1, Z2, A2

# 计算准确率
test_predictions = forward_prop(X_test.transpose())[3] # 获取输出层A2
test_comparisons = np.equal((test_predictions >= 0.5).flatten().astype(int), Y_test)
accuracy = sum(test_comparisons.astype(int)) / X_test.shape[0]
print("ACCURACY: ", accuracy)