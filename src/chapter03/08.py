def z_score(x, mean, std):
    return (x - mean) / std

def z_to_x(z, mean, std):
    return z * std + mean

# 转换为z分数
z = z_score(80, 70, 10)
print(z)

# 转换为原始值
x = z_to_x(z, 70, 10)
print(x)