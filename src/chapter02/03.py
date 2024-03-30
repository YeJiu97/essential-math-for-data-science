from scipy.stats import binom

n = 137
p = 0.4
p_50_or_more_noshows = 0.0

for x in range(50, 128):
    p_50_or_more_noshows += binom.pmf(x, n, p)

print(p_50_or_more_noshows)