import numpy as np
import pandas as pd
def cal_sta(data , freq):
	df = pd.DataFrame({'Value': data, 'Frequency' : freq})
	total = df['Frequency'].sum()
	df['Weighted_Value'] = df['Value'] * df['Frequency']
	mean = df['Weighted_Value'].sum() / total
	cumulative_frequency = df['Frequency'].cumsum()
	median_index = cumulative_frequency.searchsorted(total / 2)
	median = df['Value'][median_index]
	mode = df['Value'][df['Frequency'].idxmax()]
	variance = np.average((df['Value'] - mean) ** 2, weights=df['Frequency'])
	std_deviation = np.sqrt(variance)
	mean_deviation = np.average(np.abs(df['Value'] - mean), weights=df['Frequency'])
	q1 = np.percentile(data, 25)
	q3 = np.percentile(data, 75)
	quartile_deviation = (q3 - q1) / 2
	return {
		'Mean': mean,
		'Median': median,
		'Mode': mode,
		'Variance': variance,
		'Standard Deviation': std_deviation,
		'Mean Deviation': mean_deviation,
		'Quartile Deviation': quartile_deviation
	}

data_input = input("Enter the data values separated by commas (e.g., 10, 20, 30): ")
18
frequencies_input = input("Enter the corresponding frequencies separated by commas (e.g., 1, 2, 3): ")
data = list(map(int, data_input.split(',')))
frequencies = list(map(int, frequencies_input.split(',')))
statistics = cal_sta(data, frequencies)
for stat, value in statistics.items():
	print(f"{stat}: {value:.2f}")