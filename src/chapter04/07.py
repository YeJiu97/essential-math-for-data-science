from numpy import array

# 声明i-hat和j-hat
i_hat = array([2, 0])
j_hat = array([0, 3])

# 用i-hat和j-hat组合基矩阵
# 也需要将行转置为列
basis = array([i_hat, j_hat]).transpose()

# 声明向量v
v = array([2, 1])

# 通过使用点积变换v来创建新的向量
new_v = basis.dot(v)

print(new_v)