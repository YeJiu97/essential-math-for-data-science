from scipy.stats import norm

def critical_z_value(p):
    norm_dist = norm(loc = 0.0, scale = 1.0)
    left_tail = (1 - p) / 2
    upper_tail = 1 - left_tail
    return norm_dist.ppf(upper_tail)

print(critical_z_value(0.95))