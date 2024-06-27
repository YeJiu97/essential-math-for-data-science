import numpy as np
import pandas as pd

# 设置随机种子
np.random.seed(0)

# 生成随机数据
def generate_data(n_samples, n_features):
    X = np.random.randn(n_samples, n_features)
    y = (np.sum(X, axis=1) > 0).astype(int)  # 简单规则: 特征和大于0的为类别1
    return X, y

# Sigmoid激活函数
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Sigmoid导数，用于反向传播
def sigmoid_derivative(x):
    return sigmoid(x) * (1 - sigmoid(x))

# 神经网络类
class NeuralNetwork:
    def __init__(self, n_features):
        self.w1 = np.random.randn(n_features, 10)  # 隐藏层权重
        self.b1 = np.zeros((1, 10))  # 隐藏层偏置
        self.w2 = np.random.randn(10, 1)  # 输出层权重
        self.b2 = np.zeros((1, 1))  # 输出层偏置

    def forward(self, X):
        self.z1 = np.dot(X, self.w1) + self.b1
        self.a1 = sigmoid(self.z1)
        self.z2 = np.dot(self.a1, self.w2) + self.b2
        self.a2 = sigmoid(self.z2)
        return self.a2

    def compute_loss(self, y, y_hat):
        return -np.mean(y * np.log(y_hat) + (1 - y) * np.log(1 - y_hat))

    def backprop(self, X, y):
        m = y.size
        y_hat = self.forward(X)
        dz2 = y_hat - y.reshape(-1, 1)
        dw2 = np.dot(self.a1.T, dz2) / m
        db2 = np.sum(dz2, axis=0) / m

        dz1 = np.dot(dz2, self.w2.T) * sigmoid_derivative(self.z1)
        dw1 = np.dot(X.T, dz1) / m
        db1 = np.sum(dz1, axis=0) / m

        return dw1, db1, dw2, db2

    def update_weights(self, dw1, db1, dw2, db2, learning_rate):
        self.w1 -= learning_rate * dw1
        self.b1 -= learning_rate * db1
        self.w2 -= learning_rate * dw2
        self.b2 -= learning_rate * db2

    # 添加准确率计算
    def compute_accuracy(self, X, y):
        y_pred = self.forward(X) >= 0.5  # 将概率输出转换为类别标签
        return np.mean(y_pred.flatten() == y)

    # 更新训练方法以包括准确率
    def train(self, X, y, learning_rate=0.1, n_iterations=1000):
        for i in range(n_iterations):
            dw1, db1, dw2, db2 = self.backprop(X, y)
            self.update_weights(dw1, db1, dw2, db2, learning_rate)
            if i % 100 == 0:
                loss = self.compute_loss(y, self.forward(X))
                accuracy = self.compute_accuracy(X, y)
                print(f"Iteration {i}, Loss: {loss:.4f}, Accuracy: {accuracy:.4f}")

# 在主函数中测试模型的最终准确率
if __name__ == "__main__":
    X, y = generate_data(100, 3)  # 100个样本，每个样本3个特征
    nn = NeuralNetwork(n_features=3)
    nn.train(X, y, learning_rate=0.1, n_iterations=1000)
    final_accuracy = nn.compute_accuracy(X, y)
    print(f"Final Accuracy: {final_accuracy:.4f}")
    nn.train(X, y, learning_rate=0.1, n_iterations=1000)