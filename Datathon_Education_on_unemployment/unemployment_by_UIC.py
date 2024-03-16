import pandas as pd

import matplotlib.pyplot as plt

# Load the dataset​
unemployment_df = pd.read_csv("Datathon_Education_on_unemployment/unemployment.csv")

# Extract relevant columns for the years 2000 to 2020 and the urbanization level category​

years_columns = [f"Unemployment_rate_{year}" for year in range(2000, 2021)]

urbanization_column = "City/Suburb/Town/Rural"

data = unemployment_df[[urbanization_column] + years_columns]

# Group the data by urbanization level and calculate the average unemployment rate for each category across the years​

average_unemployment = data.groupby(urbanization_column)[years_columns].mean()

# Plot the data​

plt.figure(figsize=(10, 6))

for urbanization in average_unemployment.index:
        plt.plot(range(2000, 2021), average_unemployment.loc[urbanization], marker='o', label=urbanization)


########################

usa_data = unemployment_df[unemployment_df['Area_name'] == 'United States']
us_unemployment_rate = []
for index in range(21):
        us_unemployment_rate.append(list(usa_data[(years_columns)[index]])[0])

plt.plot(range(2000, 2021), us_unemployment_rate, linestyle='--', label='US Average')

########################

plt.xticks(list(range(2000, 2021, 2)))

plt.title('Average Unemployment Rate by Urbanization Level (2000-2020)')
plt.xlabel('Year')
plt.ylabel('Average Unemployment Rate')
plt.legend()
plt.grid(True)
plt.show()