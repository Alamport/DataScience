###############################################################################
# unemplyment_by_UIC.py                                    
#
# The program aims to discover how unemployment rates have changed throughout a # lenght of 20 years (2020 - 2022) in different urbanization levels. The 
# conclusion fromm the data state comfortably that suburban areas always 
# struggle the most compared to other areas and rural areas remain the least
# affected. One reasoning regarding the latter is that people who work in rural
# areas have jobs that are a necessity to society, such as farming. So when
# the economy of the country falls, as these jobs are indispensable, workers in 
# rural areas are not laid off.
#
# Adin Lamport (March, 2024)
###############################################################################
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