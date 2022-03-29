import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('cars.csv')

#print(df.head())

sns.displot(df, x='price_usd', hue='manufacturer_name')

plt.show()