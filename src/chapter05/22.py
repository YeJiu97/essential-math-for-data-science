import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf

# Load the data
data = pd.read_csv('https://bit.ly/2KF29Bd', delimiter=",")
# Assuming the column names in the CSV are 'x' for the independent variable and 'y' for the dependent variable

# Fit linear regression model using statsmodels
model = smf.ols('y ~ x', data=data).fit()

# Predict at a new data point, e.g., x = 8.5
x_new = pd.DataFrame({'x': [8.5]})
predictions = model.get_prediction(x_new)

# Get the prediction summary which includes the prediction interval
prediction_summary = predictions.summary_frame(alpha=0.05)  # 95% confidence and prediction intervals
print(prediction_summary)
