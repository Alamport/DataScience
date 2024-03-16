import pandas as pd

import matplotlib.pyplot as plt

# loads the dataset​
df = pd.read_csv("Datathon_Education_on_unemployment/education.csv") 

# extracts relevant columns​
urbanization_column = "City/Suburb/Town/Rural 2013"

education_columns = [
        "Percent of adults with less than a high school diploma, 2015-19",
        "Percent of adults with a high school diploma only, 2015-19",
        "Percent of adults completing some college or associate's degree, 2015-19",
        "Percent of adults with a bachelor's degree or higher, 2015-19"
]

# groups the data by urbanization level and calculate the average percent of education level for each category​
average_education = df.groupby(urbanization_column)[education_columns].mean()

# calculates the national average of each education level across all urbanization levels​
national_average = df[education_columns].mean()

# adds a row for national average to the average_education DataFrame​
average_education.loc['National Average'] = national_average

# plots the data​
plt.figure(figsize=(10, 6))

index = list(average_education.index)
x = range(len(index))

# plots stacked bar chart for each urbanization level​
bottom = None

for i, column in enumerate(education_columns):

        plt.bar(index, average_education[column], bottom=bottom, label=column)

        if bottom is None:
                bottom = average_education[column]
        else:
                bottom += average_education[column]

                plt.xlabel('Urbanization Level')

                plt.ylabel('Average Percent of Education Level')

                plt.title('Average Percent of Education Level by Urbanization Level')


# places the legend outside the plot​
plt.legend(["Less than a high school diploma", "High school diploma only", "Some college or associate's degree", "Bachelor's degree or higher"] ,loc='center left', bbox_to_anchor=(1, 0.5))
plt.tight_layout()
plt.savefig("education_level_by_area.png")
plt.show()