from scipy.stats import norm

# 感冒有18天的平均恢复期，1.5天的标准差
mean = 18
std_dev = 1.5

# 恢复期的95%置信区间
confidence_interval = norm.interval(0.95, loc = mean, scale = std_dev)
print(confidence_interval)

# H0: 平均恢复期>=18天
# H1: 平均恢复期<18天

# 单边检验
# 什么样的x值左边有5%的面积
x = norm.ppf(0.05, loc = mean, scale = std_dev)
print(x)

# 双边检验
# 什么样的x值左边有2.5%的面积
x = norm.ppf(0.025, loc = mean, scale = std_dev)
# 什么样的x值右边有2.5%的面积
y = norm.ppf(0.975, loc = mean, scale = std_dev)
print(x, y)

# 计算双尾p值
# <16 and >20
p = norm.cdf(16, loc = mean, scale = std_dev) + (1 - norm.cdf(20, loc = mean, scale = std_dev))
print(p)