from numpy import array

# 变换1
i_hat1 = array([0, 1])
j_hat1 = array([-1, 0])
transform1 = array([i_hat1, j_hat1]).transpose()
print("TRANSFORM1 MATRIX:\n {}".format(transform1))

# 变换2
i_hat2 = array([1, 0])
j_hat2 = array([1, 1])
transform2 = array([i_hat2, j_hat2]).transpose()
print("TRANSFORM2 MATRIX:\n {}".format(transform2))

# 合并两个变换
combined = transform2 @ transform1

# 测试
print("COMBINED MATRIX:\n {}".format(combined))

v = array([1, 2])
print(combined.dot(v))

# 分批进行
rotated = transform1.dot(v)
print("ROTATED: {}".format(rotated))
translated = transform2.dot(rotated)
print("TRANSLATED: {}".format(translated))