import random
from scipy.stats import norm

for i in range(0, 1000):
    random_p = random.uniform(0, 1)
    random_weight = norm.ppf(random_p, 64.43, 2.99)
    print(random_weight)