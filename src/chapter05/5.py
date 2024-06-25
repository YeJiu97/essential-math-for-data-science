# 计算给定直线和数据的平方和
import pandas as pd

# 读取数据
points = pd.read_csv('https://bit.ly/3goOAnt', delimiter = ',').itertuples()

# 根据给定的直线执行测试
m = 1.93
b = 4.73

sum_of_squares = 0.0

# 计算平方和
for p in points:
    y_actual = p.y
    y_predict = m*p.x + b
    residual = y_actual - y_predict
    sum_of_squares += residual**2

print(f"sum of squares: {sum_of_squares}")