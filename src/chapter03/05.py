import math
# PDF: probability density function
def normal_pdf(x:float, mean:float, std_dev:float) -> float:
    return (1 / (std_dev * (2 * math.pi) ** 0.5)) * math.exp(-((x - mean) ** 2) / (2 * std_dev ** 2))