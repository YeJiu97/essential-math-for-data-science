import pandas as pd

df = pd.read_csv('https://bit.ly/2KF29Bd', delimiter = ',')

# 变量之间的相关性系数
correlations = df.corr(method='pearson')  # 皮尔逊相关系数，是一种线性相关系数，用于度量两个变量之间的线性相关程度

print(correlations)