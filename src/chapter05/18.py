from scipy.stats import t
from math import sqrt

# 样本数量
n = 10

# 计算临界值
lower_cv = t.ppf(0.025, df=n-1)
upper_cv = t.ppf(0.975, df=n-1)  # 注意：这里应该是0.975，而不是0.025

# 相关性系数
r = 0.957586

# 实施检验
test_value = r * sqrt((n - 2) / (1 - r ** 2))
print(test_value)

print("TEST VALUE: {:.4f}".format(test_value))
print("CRITICAL RANGE: {:.4f}, {:.4f}".format(lower_cv, upper_cv))

if test_value < lower_cv or test_value > upper_cv:
    print("Reject the null hypothesis")
else:
    print("Fail to reject the null hypothesis")

# 计算p值
if test_value > 0:
    p_value = 2 * (1 - t.cdf(test_value, df=n-1))
else:
    p_value = 2 * t.cdf(test_value, df=n-1)

print("P VALUE: {:.4f}".format(p_value))