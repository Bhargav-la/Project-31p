import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

deliveries = pd.read_csv('deliveries.csv')
matches = pd.read_csv('matches.csv')

deliveries.head()
print(deliveries.head())
matches.head()
print(matches.head())
deliveries.isnull().sum()
print(deliveries.isnull().sum())
matches.isnull().sum()
print(matches.isnull().sum())

sns.heatmap(deliveries.isnull())
plt.show()

sns.heatmap(matches.isnull())
plt.show()

deliveries.dropna(inplace=True)
print(deliveries.isnull().sum())

matches.dropna(inplace=True)
print(matches.isnull().sum())

deliveries.drop(columns=['player_dismissed','fielder','dismissal_kind'], inplace=True)
matches.drop(columns=['umpire3'], inplace=True)
