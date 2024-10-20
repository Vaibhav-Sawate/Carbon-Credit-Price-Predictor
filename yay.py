import pandas as pd
import numpy as np

# Create a date range
dates = pd.date_range(start='1/1/2020', end='12/31/2023', freq='M')

# Generate random data
np.random.seed(0)
data = {
    'Date': dates,
    'Carbon_Price': np.random.uniform(20, 50, len(dates)),
    'CO2_Emissions': np.random.uniform(1000, 2000, len(dates)),
    'GDP': np.random.uniform(50000, 100000, len(dates)),
    'Oil_Price': np.random.uniform(40, 80, len(dates)),
    'Coal_Price': np.random.uniform(20, 40, len(dates)),
    'Gas_Price': np.random.uniform(2, 4, len(dates)),
    'Renewable_Energy_Index': np.random.uniform(50, 100, len(dates)),
    'Temperature': np.random.uniform(10, 25, len(dates)),
    'Trading_Volume': np.random.uniform(10000, 50000, len(dates)),
    'Regulatory_Changes': np.random.randint(0, 2, len(dates)), # 0 or 1 indicator
    'Technological_Advances': np.random.randint(0, 2, len(dates)), # 0 or 1 indicator
    'Global_Events': np.random.randint(0, 2, len(dates)) # 0 or 1 indicator
}

# Create DataFrame
df = pd.DataFrame(data)

# Save to a CSV file
df.to_csv('carbon_credit_prices.csv', index=False)

print(df.head())
