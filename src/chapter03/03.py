# 生成样本
import random
sample = [random.randint(0, 100) for _ in range(10)]

# 中位数
sample.sort()
n = len(sample)
if n % 2 == 0:
    median = (sample[n//2-1] + sample[n//2]) / 2
else:
    median = sample[n//2]
print(median)

# 众数
from collections import Counter
c = Counter(sample)
print(c)
mode = c.most_common(1)[0][0]
print(mode)