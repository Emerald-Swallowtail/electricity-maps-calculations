import pandas as pd
import statistics

df = pd.read_csv('data/DE_2023_hourly.csv')

carbon_intensity_values = df['Carbon Intensity gCO₂eq/kWh (direct)']

mean = statistics.mean(carbon_intensity_values)

print("Mean of 2023")
print(mean)