import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

diamonds= pd.read_csv('diamonds.csv')

def outliers(df, column):
    Q1= np.quantile(df[column], 0.25)
    Q3= np.quantile(df[column], 0.75)
    IQR= Q3 - Q1
    lower_threshold= Q1 - 1.5 * IQR
    upper_threshold= Q3 + 1.5 * IQR
    outliers= df[(df[column] < lower_threshold) | (df[column] > upper_threshold)]
    return outliers


outliers_price= outliers(diamonds, 'price')
outliers_carat= outliers(diamonds, 'carat')


print("Summary statistics of Outlier Diamonds based on Price")
print(outliers_price.describe())
print("Summary statistics of Outlier Diamonds based on Carat")
print(outliers_carat.describe())
print("Summary statistics for the rest data")
print(~(diamonds.reset_index()['index'].isin(list(outliers_price.index) + list(outliers_carat.index))))


sns.boxplot(data=diamonds,
            x='price')

plt.show()

plt.clf()

sns.boxplot(data=diamonds,
            x='carat')

plt.show()