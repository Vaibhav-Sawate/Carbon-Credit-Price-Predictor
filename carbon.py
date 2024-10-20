import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pickle

# Load the dataset
df = pd.read_csv('carbon_credit_prices.csv')

# Define features and target variable
X = df[['CO2_Emissions', 'GDP', 'Oil_Price', 'Coal_Price', 'Gas_Price', 'Renewable_Energy_Index', 'Temperature', 'Trading_Volume', 'Regulatory_Changes', 'Technological_Advances', 'Global_Events']]
y = df['Carbon_Price']

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

# Train the model
lr = LinearRegression()
lr.fit(X_train, y_train)

# Save the model
pickle.dump(lr, open('carbon_model.pkl', 'wb'))
