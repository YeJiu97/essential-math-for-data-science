from scipy.stats import t

n = 10
lower_cv = t(n-1).ppf(0.025)
upper_cv = t(n-1).ppf(0.975)

print(lower_cv, upper_cv)
