import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv('tatas.csv', encoding='latin1') 


print("Initial data overview:")
print(df.head())  
print("\nData info:")
print(df.info()) 
print("\nSummary statistics:")
print(df.describe()) 





plt.figure(figsize=(8, 6))
sns.histplot(df['Quantity'], bins=20, kde=True)
plt.title('Distribution of Quantity')
plt.xlabel('Quantity')
plt.ylabel('Frequency')
plt.show()


plt.figure(figsize=(12, 6))
sns.countplot(x='Country', data=df)
plt.title('Count of Orders by Country')
plt.xlabel('Country')
plt.ylabel('Count')
plt.xticks(rotation=90)
plt.show()


