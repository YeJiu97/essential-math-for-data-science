# 每个人拥有的宠物的数量
animals = {1, 3, 4, 7, 6, 2}

# 开始计算方差
n = len(animals)
mean = sum(animals) / n
variance = sum((x - mean) ** 2 for x in animals) / n
print(variance)

# 标准差,不适用math库
def variance(value, is_sample=False):
    n = len(value)
    mean = sum(value) / n
    return sum((x - mean) ** 2 for x in value) / (n - int(is_sample))


# 计算样本的方差，n-1
variance = sum((x - mean) ** 2 for x in animals) / (n - 1)
print(variance)

# 计算样本的标准差
def standard_deviation(value, is_sample=True):
    return variance(value, is_sample) ** 0.5
print(standard_deviation(animals))