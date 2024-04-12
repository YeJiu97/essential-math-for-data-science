import pandas as pd

# 读取数据
points = pd.read_csv('https://bit.ly/3goOAnt', delimiter=',').itertuples()

# 根据给定直线执行测试
m = 1.9393
b = 4.7333

sum_of_squares = 0

# 计算平方和
for p in points:
    y_actual = p.y
    y_predict = m * p.x + b
    residuals = y_actual - y_predict
    sum_of_squares += residuals ** 2

print(f'平方和: {sum_of_squares}')