import pandas as pd
from sklearn.linear_model import LinearRegression
import statsmodels.api as sm
from statsmodels.sandbox.regression.predstd import wls_prediction_std

# 加载数据
df = pd.read_csv('https://bit.ly/2X1HWH7', delimiter=",")
X = df.values[:, :-1]
Y = df.values[:, -1]

# 添加常数项以拟合截距
X = sm.add_constant(X)

# 使用sklearn的LinearRegression计算R^2
model_sklearn = LinearRegression().fit(X, Y)
print("R^2 = {0}".format(model_sklearn.score(X, Y)))

# 使用statsmodels进行回归分析
model_sm = sm.OLS(Y, X).fit()
print("Coefficients = \n", model_sm.summary())

# 计算95%的置信区间
predictions = model_sm.get_prediction(X)
prediction_summary = predictions.summary_frame(alpha=0.05)
print("95% 置信区间 = \n", prediction_summary[['obs_ci_lower', 'obs_ci_upper']])
