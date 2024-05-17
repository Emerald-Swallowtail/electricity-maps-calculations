import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file into a DataFrame
df22 = pd.read_csv('data/DE_2022_hourly.csv')
df23 = pd.read_csv('data/DE_2023_hourly.csv')

# Extract the 'Datetime (UTC)' and 'Carbon Intensity' columns
datetime_values_22 = pd.to_datetime(df22['Datetime (UTC)'])
carbon_intensity_values_22 = df22['Carbon Intensity gCO₂eq/kWh (direct)']

datetime_values_23 = pd.to_datetime(df22['Datetime (UTC)'])
carbon_intensity_values_23 = df23['Carbon Intensity gCO₂eq/kWh (direct)']

# Set the figure size to make the plot wider
plt.figure(figsize=(12, 6))  # Adjust the width and height as needed

# Plot the 'Carbon Intensity' values against 'Datetime (UTC)'
plt.plot(datetime_values_22, carbon_intensity_values_22)
plt.xlabel('Datetime (UTC)')
plt.ylabel('gCO₂eq/kWh (direct)')
plt.title('Carbon Intensity Germany 2022')

# Annotate the plot with minimum and maximum values
min_intensity = carbon_intensity_values_22.min()
max_intensity = carbon_intensity_values_22.max()
plt.text(datetime_values_22.iloc[0], min_intensity, f'Min: {min_intensity}', va='bottom')
plt.text(datetime_values_22.iloc[-1], max_intensity, f'Max: {max_intensity}', ha='right', va='top')

# Save the plot to a PNG file
plt.savefig('data/carbon_intensity_plot22.png')

# Plot the 'Carbon Intensity' values against 'Datetime (UTC)'
plt.plot(datetime_values_23, carbon_intensity_values_23)
plt.xlabel('Datetime (UTC)')
plt.ylabel('gCO₂eq/kWh (direct)')
plt.title('Carbon Intensity Germany 2023')

# Annotate the plot with minimum and maximum values
min_intensity = carbon_intensity_values_23.min()
max_intensity = carbon_intensity_values_23.max()
plt.text(datetime_values_23.iloc[0], min_intensity, f'Min: {min_intensity}', va='bottom')
plt.text(datetime_values_23.iloc[-1], max_intensity, f'Max: {max_intensity}', ha='right', va='top')

# Save the plot to a PNG file
plt.savefig('data/carbon_intensity_plot2223.png')