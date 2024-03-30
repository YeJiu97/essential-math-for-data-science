from sympy import *

# 4x + 2y + 4z = 44
# 5x + 3y + 7z = 56
# 9x + 3y + 6z = 72

# A矩阵
A = Matrix([
    [4, 2, 4],
    [5, 3, 7],
    [9, 3, 6]
])

# A和其逆矩阵之间的点积
# 将产生单位函数
inverse_A = A.inv()
identity = A * inverse_A

# 打印
print(identity)
print(inverse_A)

# 求解方程组
# B矩阵
B = Matrix([44, 56, 72])

# 解方程组
X = A.inv() * B
print(X)
