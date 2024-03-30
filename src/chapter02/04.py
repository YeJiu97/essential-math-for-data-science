from scipy.stats import beta

a = 19
b = 4

p = 1 - beta.cdf(0.5, a, b)
print(p)