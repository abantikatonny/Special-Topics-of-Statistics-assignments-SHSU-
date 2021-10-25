import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# function for getting the weekly data from the daily data
def reduce_to_weekly(input_list):
    weekly_count = []
    temp_sum = 0
    counter = 0

    for i, value in enumerate(input_list):
        temp_sum = temp_sum + input_list[i]
        counter += 1

        if counter % 7 == 0:
            weekly_count.append(temp_sum)
            temp_sum = 0

    if temp_sum > 0:
        weekly_count.append(temp_sum)

    return weekly_count


# import the data file
data = pd.read_csv('C:/Users/Abantika/Programming/practise/data_master.csv', delimiter=',')

# make a list of the countries
country_list = ['Australia', 'United States of America','The United Kingdom', 'Brazil', 'Russian Federation', 'Japan', 'France', 'Germany', 'Egypt', 'Viet Nam', 'India', 'Italy']

# creating a database for japan because it has the highest date_reported data
japan_database = data[data['Country'] == 'Japan']
date_range_for_Japan = list(japan_database['Date_reported'])

#  creating a data list from March to end of the August
filtered_date_list = []
for i_date in date_range_for_Japan:
    if i_date[0] == '3' or i_date[0] == '4' or i_date[0] == '5' or i_date[0] == '6' or i_date[0] == '7' or i_date[0] == '8':
        filtered_date_list.append(i_date)


# Making a list which will collect the new cases according to every country
boxplot_input_data = []

for temp_country in country_list:

    new_case_count_for_country = []

    for temp_date in filtered_date_list:

        data_for_temp_country = data[data['Country'] == temp_country]
        data_for_temp_date = data_for_temp_country[data_for_temp_country['Date_reported'] == temp_date]
        temp_new_case = list(data_for_temp_date['New_cases'])[0]
        new_case_count_for_country.append(temp_new_case)

    # Calling the weekly conversion function
    reduced_data = reduce_to_weekly(new_case_count_for_country)

    boxplot_input_data.append(reduced_data)


# define the figure size
plt.figure(figsize=(12, 6))
plt.boxplot(boxplot_input_data)

# plotting label and data range
labels = country_list

plt.xticks([1,2,3,4,5,6,7,8,9,10,11,12], labels, rotation= 45 )

plt.tight_layout()
plt.show()
