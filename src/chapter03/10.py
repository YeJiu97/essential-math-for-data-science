# 在Python中计算置信区间
from math import sqrt
from scipy.stats import norm

p = 0.95
sample_mean = 64.408
sample_std = 2.05
n = 31

z = norm.ppf((1 + p) / 2)
margin_of_error = z * sample_std / sqrt(n)
confidence_interval = (sample_mean - margin_of_error, sample_mean + margin_of_error)
print(confidence_interval)

# 直接使用scipy.stats.norm.interval
confidence_interval = norm.interval(p, loc = sample_mean, scale = sample_std / sqrt(n))
print(confidence_interval)