# b = R-1 Qt y
import numpy as np
import pandas as pd
from numpy.linalg import inv, qr

# Load data
df = pd.read_csv('https://bit.ly/3goOAnt', delimiter=',')

# Extract input variables
X = df.values[:, :-1].flatten()

# Add a column of ones as a placeholder for the intercept
X_1 = np.array([np.ones(len(X)), X]).T

# Extract the input column
Y = df.values[:, -1]

# Calculate the slope and intercept coefficients
Q, R = qr(X_1)
b = inv(R) @ Q.T @ Y

print(f'Correlation coefficient: {b[1]}')
print(f'Intercept: {b[0]}')