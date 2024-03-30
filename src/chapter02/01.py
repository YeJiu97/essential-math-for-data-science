# 使用SciPy实现二项分布
# 二项分布是n个独立的是/非试验中成功的次数的离散概率分布
from scipy.stats import binom

n = 10
p = 0.9

for k in range(n + 1):
    probability = binom.pmf(k, n, p)
    print( "{0} : {1} ".format(k, probability))