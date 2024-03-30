from scipy.stats import norm

mean = 64.43
std_dev = 2.99

x = norm.cdf(64.43, mean, std_dev)

print(x)

# 得到某一个中间区域的概率
x = norm.cdf(68, mean, std_dev) - norm.cdf(63, mean, std_dev)
print(x)

# 逆cdf,也就是ppf，用来得到某一个概率对应的值
x = norm.ppf(0.95, mean, std_dev)
print(x)