import pandas as pd
import statistics

df22 = pd.read_csv('data/DE_2022_hourly.csv')
df23 = pd.read_csv('data/DE_2023_hourly.csv')

ci22 = df22['Carbon Intensity gCO₂eq/kWh (direct)']
ci23 = df23['Carbon Intensity gCO₂eq/kWh (direct)']


mean22 = statistics.mean(ci22)
print("Mean of 2022")
print(mean22)

mean23 = statistics.mean(ci23)
print("Mean of 2023")
print(mean23)