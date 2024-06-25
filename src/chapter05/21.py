import pandas as pd
from scipy.stats import t
from math import sqrt

# Load the data
data = pd.read_csv('https://bit.ly/2KF29Bd', delimiter=",")
points = list(data.itertuples())
n = len(points)

# Linear Regression Line coefficients
m = 1.939
b = 4.733

# Calculate Prediction Interval for x = 8.5
x_0 = 8.5
x_mean = sum(p.x for p in points) / n
t_value = t.ppf(0.975, df=n - 2)  # df is degrees of freedom, n-2 for simple linear regression

# Sum of squares of x for denominator in margin of error formula
sum_x_squared = sum(p.x ** 2 for p in points)
sum_x = sum(p.x for p in points)

# Standard error of the estimate
sse = sum((p.y - (m * p.x + b)) ** 2 for p in points)  # Sum of squared errors
standard_error = sqrt(sse / (n - 2))

# Margin of error
margin_of_error = t_value * standard_error * sqrt(
    1 + (1 / n) + (n * (x_0 - x_mean) ** 2) / (n * sum_x_squared - sum_x ** 2)
)

# Predicted y value
predicted_y = m * x_0 + b

# Output prediction interval
lower_bound = predicted_y - margin_of_error
upper_bound = predicted_y + margin_of_error
print(f"Prediction interval for x = {x_0}: {lower_bound}, {upper_bound}")
