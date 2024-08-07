import pandas as pd
# Read data into Pandas dataframe
df = pd.read_csv('https://bit.ly/2KF29Bd', delimiter=",")
# Print correlations between variables
coeff_determination = df.corr(method='pearson') ** 2
print(coeff_determination)