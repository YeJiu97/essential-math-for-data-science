from numpy import array

# 变换1
i_hat1 = array([0, 1])
j_hat1 = array([-1, 0])
transform1 = array([i_hat1, j_hat1]).transpose()

# 变换2
i_hat2 = array([1, 0])
j_hat2 = array([1, 1])
transform2 = array([i_hat2, j_hat2]).transpose()

# 合并两个变换，首先应用剪切，然后应用旋转
combined = transform1 @ transform2

# 测试
print("COMBINED MATRIX:\n {}".format(combined))

# 用于测试的向量
v = array([1, 2])
print(combined.dot(v))