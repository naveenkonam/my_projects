import matplotlib.pyplot as plt
import pandas as pd

file = '/home/konam/Desktop/constdata.xlsx'

df = pd.read_excel(file)

print(df.head())

print(df.columns)

plt.bar(df['Date'],df['RCC'])
plt.title("RCC chart")
plt.xaxis("Date")
plt.show()
