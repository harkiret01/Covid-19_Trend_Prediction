import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')
from scipy.optimize import curve_fit
from matplotlib import pyplot
from datetime import datetime, timezone, timedelta
from numpy import arange

# define the true objective function
def objective(x, a, b, c):
	return a * x + b * x**2 + c

dataFrame = pd.read_csv("COVID-19_case_counts_by_date_half.csv")
dataFrame2 = pd.read_csv("COVID-19_case_counts_by_date.csv")
print(dataFrame.shape) 
dataFrame.head()

dataFrame['Days'] = np.arange(len(dataFrame))
dataFrame2['Days'] = np.arange(len(dataFrame2))
dataFrame['Date'] = pd.to_datetime(dataFrame['Date'])

dataFrame2['Date'] = pd.to_datetime(dataFrame2['Date'])


data = dataFrame.values
data = dataFrame2.values


x = dataFrame['Days']
y = dataFrame['Total_cases']
i = dataFrame2['Days']
j = dataFrame2['Total_cases']

# curve fit
popt, _ = curve_fit(objective, x, y)
# summarize the parameter values
a, b, c = popt
print('Equation: y = %.5f * x + %.5f * x^2 + %.5f' % (a, b, c))
# plot input vs output

pyplot.scatter(i, j, label="6 months")
pyplot.scatter(x, y, label="3 months")

# define a sequence of inputs between the smallest and largest known inputs
x_line = arange(min(x), max(i), 1)
# calculate the output for the range
y_line = objective(x_line, a, b, c)
# create a line plot for the mapping function
pyplot.plot(x_line, y_line, '--', label='prediction', color='red')
pyplot.legend()
pyplot.title('Total Covid 19 cases')
plt.xlabel('Days (s)')
plt.ylabel('Number of cases')
pyplot.show()

