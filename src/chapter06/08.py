import math

# 设定事件发生的概率 P
P = 0.75  # 事件发生的概率

# 计算几率
odds = P / (1 - P)

# 计算对数几率（log-odds），使用自然对数
log_odds = math.log(odds)

print(f"概率: {P}")
print(f"几率: {odds}")
print(f"对数几率: {log_odds}")
