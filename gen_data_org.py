###############################################################################
# gen_data_org.py                                    
#
# This file aims to create generic code that can be easily copied and pasted
# for future uses. Here are the following sections:
#       1) Reading in a csv file
#       2) Columns of interest
#               a) Repeating column names
#       3) Filtering the data
#       4) Finding stat about some data
#       5) Setting the graph
#
# Adin Lamport (March, 2024)
###############################################################################
# Empty code to be used later
urbanization_column = []
edu_cols = []
years_columns = []
###############################################################################
import pandas as pd
import matplotlib.pyplot as plt 

plt.style.use('fivethirtyeight')

"""                    Reading in a csv file                                 """
data = pd.read_csv('filename.csv')


"""                    Columns of data that is of interest                   """
columns_of_interest = {
        'FIPS_Code',
        'Unemployment_rate_2000',
        'Unemployment_rate_2001'
}


"""                    Columns of data with repeating names                  """
repeated_interest = [f"Unemployment_rate_{year}" for year in range(2000, 2021)]
# OR
years = [2000, 2001, 2002, 2003]
repeated_interest2 = [f"Unemployment_rate_{year}" for year in years]


""""                   Filtering the data                                    """
# gets all entries where the data contains "NY" as its state
filtered_data = data[data['State'] == 'NY']
unemployment_rate_NY = filtered_data[columns_of_interest]


"""                    Finding stat of some sorted data                      """
# groups data by urbanization lvl & calcs the avg % of edu lvl for each category
average_education = data.groupby(urbanization_column)[edu_cols].mean()

# groups data by urb. lvl & calcs the avg unemplyment rate for each category across the years
average_unemployment = data.groupby(urbanization_column)[years_columns].mean()


"""                    Setting the graph                                     """
line_names = ["First", "Second", "Third"]
plt.legend(line_names ,loc='center left', bbox_to_anchor=(1, 0.5))
# in the example below, have a label written in each plot 
        # this is better since if we change order of plots, the legend would be 
        # wrong in the other version
plt.legend()


plt.title("TITLE")
plt.xlabel("X AXIS")
plt.ylabel("Y AXIS")

# ensures that the figure has a nice layout
plt.tight_layout()  

# if having a grid would be helpful for visualization
# plt.grid(True)

# plt.savefig('NAME.png')
plt.show()