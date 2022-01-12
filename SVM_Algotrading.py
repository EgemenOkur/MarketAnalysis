# Machine learning
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

# For data manipulation
import pandas as pd
import numpy as np

from pandas_datareader import data

# Only get the adjusted close.
df = data.DataReader("U",
                       start='2019-12-1',
                       end='2022-01-10',
                       data_source='yahoo')



# saving the dataframe
df.to_csv('AAPL.csv')

# To plot
import matplotlib.pyplot as plt
plt.style.use('seaborn-darkgrid')

# To ignore warnings
import warnings
warnings.filterwarnings("ignore")

#df = pd.read_csv('BANKING_STOCK.csv')
# Read the csv file using read_csv
# method of pandas
# Changes The Date column as index columns
#df.index = pd.to_datetime(df['Date'])
# drop The original date column
#df = df.drop(['Date'], axis='columns')

# Create predictor variables
df['Open-Close'] = df.Open - df.Close
df['High-Low'] = df.High - df.Low

# Store all predictor variables in a variable X
X = df[['Open-Close', 'High-Low']]
X.head()

# Target variables
y = np.where(df['Close'].shift(-1) > df['Close'], 1, 0)

split_percentage = 0.8
split = int(split_percentage * len(df))

# Train data set
X_train = X[:split]
y_train = y[:split]

# Test data set
X_test = X[split:]
y_test = y[split:]

# Support vector classifier
cls = SVC().fit(X_train, y_train)
df['Predicted_Signal'] = cls.predict(X)
# Calculate daily returns
df['Return'] = df.Close.pct_change()


# Calculate Cumulutive returns
df['Cum_Ret'] = df['Return'].cumsum()

# Calculate strategy returns
df['Strategy_Return'] = df.Return *df.Predicted_Signal.shift(1)

# Plot Strategy Cumulative returns
df['Cum_Strategy'] = df['Strategy_Return'].cumsum()

import matplotlib.pyplot as plt

plt.plot(df['Cum_Ret'],color='red')
plt.plot(df['Cum_Strategy'],color='blue')
plt.show()


#print(accuracy_score(y_test, X_test))