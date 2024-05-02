import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file into a DataFrame
df = pd.read_csv('data/DE_2023_hourly.csv')

# Extract the 'LCP' column
lcp_values = df['Low Carbon Percentage']

plt.hist(lcp_values, bins=10, edgecolor='black')  # Adjust the number of bins as needed
plt.xlabel('Low Carbon Energy Percentage')
plt.ylabel('Frequency (1hr periods)')
plt.title('Histogram of LCP Values for Germany 2023')

# Save the plot to a PNG file
plt.savefig('data/histogram.png')
