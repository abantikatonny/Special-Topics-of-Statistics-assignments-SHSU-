import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# import database and country list
data = pd.read_csv('C:/hmm/courses/3rd semester/Special topics/Assignment 1/data_master.csv', delimiter=',')
country_list = ['Australia', 'United States of America', 'The United Kingdom', 'Brazil', 'Russian Federation', 'Japan', 'France', 'Germany', 'Egypt', 'Viet Nam', 'India', 'Italy' ]

# define figure size
plt.figure(figsize=(10,6))

# creating a new database for the country in country list
for country in country_list:
    get_Country = (data['Country']== country)
    new_database = data[get_Country]

    # plotting the data from database
    plt.plot(new_database['Date_reported'], new_database['New_cases'], label=country)

# creating labels
plt.xlabel('Date Reported')
plt.ylabel('New Cases')

# creating a database for japan because it has the highest date_reported data
for country in country_list:
        another_database = (data['Country']=='Japan')
        japan_database = data[another_database]
        date_range_for_japan = japan_database['Date_reported']

# plotting label and data range
labels = []
for i in np.arange(0, len(date_range_for_japan), 8):
    labels.append(data['Date_reported'][i])

#plotting the date range vertically
plt.xticks(np.arange(0, len(date_range_for_japan), 8), labels, rotation='vertical' )

plt.legend()
plt.tight_layout()
plt.show()



