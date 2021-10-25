import numpy as np
import pandas as pd
import scipy.stats

# import the data file
data = pd.read_csv('C:/hmm/courses/3rd semester/Special topics/Assignment 1/data_master.csv', delimiter=',')

# creating a database for US because it has the highest date_reported data
States_database = data[data['Country'] == 'United States of America']
date_range_for_States = list(States_database['Date_reported'])

filtered_date_list = []
for i_date in date_range_for_States:
    if i_date[0] == '3' or i_date[0] == '4' or i_date[0] == '5' or i_date[0] == '6' or i_date[0] == '7' or i_date[0] == '8':
        filtered_date_list.append(i_date)


def compute_correlation_coefficient(country1, country2):
    """
    This function computes and returns the Pearson correlation coefficient between the daily new cases of the given
    two countries.

    param1 (string): The first country
    :param country2: Second country

    Returns:
        float: Pearson correlation coefficient
    """

    new_case_count_for_country1 = []
    new_case_count_for_country2 = []

    # Accumulating new case counts for country1
    for temp_date in filtered_date_list:
        data_for_temp_country = data[data['Country'] == country1]
        data_for_temp_date = data_for_temp_country[data_for_temp_country['Date_reported'] == temp_date]

        temp_new_case = list(data_for_temp_date['New_cases'])[0]
        new_case_count_for_country1.append(temp_new_case)


    for temp_date in filtered_date_list:
        data_for_temp_country = data[data['Country'] == country2]
        data_for_temp_date = data_for_temp_country[data_for_temp_country['Date_reported'] == temp_date]

        temp_new_case = list(data_for_temp_date['New_cases'])[0]
        new_case_count_for_country2.append(temp_new_case)

    # Compute correlation coefficient
    correlation_coefficient = scipy.stats.pearsonr(new_case_count_for_country1, new_case_count_for_country2)[0]

    return round(correlation_coefficient, 4)



pairs_to_evaluate = [
    ['Australia', 'United States of America'],
    ['The United Kingdom', 'United States of America'],
    ['Brazil', 'United States of America'],
    ['India', 'United States of America'],
    ['Egypt', 'United States of America'],
    ['Viet Nam', 'United States of America'],
    ['Russian Federation', 'United States of America'],
    ['Italy', 'United States of America'],
]


for country1, country2 in pairs_to_evaluate:
    print('Correlation coefficient for {} and {} is '.format(country1, country2), compute_correlation_coefficient(country1, country2))

