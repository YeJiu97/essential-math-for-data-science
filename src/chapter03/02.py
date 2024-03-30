# 加权平均
sample = [1, 2, 3, 4, 5]
weights = [5, 4, 3, 2, 1]

# 加权平均
wmean = sum(w * v for w, v in zip(weights, sample)) / sum(weights)

# 打印
print(wmean)