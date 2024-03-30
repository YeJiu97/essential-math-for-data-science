from numpy import array

# 声明i-hat和j-hat
i_hat = array([2, 0])
j_hat = array([0, 3])

# 将两者组成基矩阵
basis = array(
    [i_hat, j_hat]
)
print(basis)

# 需要将行向量转置
basis = array([i_hat, j_hat]).transpose()
print(basis)