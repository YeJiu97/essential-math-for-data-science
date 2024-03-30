from numpy import array

# 由i-hat和j-hat组成基矩阵
basis = array(
    [[3, 0],
     [0, 2]]
)

# 声明向量v
v = array([1, 1])

# 通过使用点积变换v来创建新向量
new_v = basis.dot(v)
print(new_v)  # [3, 2]