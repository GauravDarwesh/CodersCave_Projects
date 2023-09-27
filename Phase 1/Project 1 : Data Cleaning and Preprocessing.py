import pandas as pd


df = pd.read_csv('amazon.csv')


print("Initial data overview:")
print(df.head())  
print("\nData info:")
print(df.info())  
print("\nSummary statistics:")
print(df.describe())  


df.dropna(inplace=True)
