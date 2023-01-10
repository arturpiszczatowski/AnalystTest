import os
import pandas as pd
import numpy as np


# simple function for counting average of two variables
def correction(a, b):
    return (a + b) / 2.0


df = pd.read_csv(os.path.abspath('task 1/UK_Temperatures.csv'),
                 header=0)
df.rename(columns={'Unnamed: 0': 'DATETIME'}, inplace=True)

# City names excluding DATETIME column
city_names = df.columns[1:]

# Replacing NaN with mean value of two neighbouring values (if available)
# If last value not available NaN is replaced with previous value
# If first value not available NaN is replaced with next value
for city in city_names:
    for index, value in enumerate(df[city]):
        if np.isnan(value):
            if index == 0:
                value = df[city][index + 1]
            elif index == len(df[city]) - 1:
                value = df[city][index - 1]
            else:
                value = correction(df[city][index - 1], df[city][index + 1])

            df.loc[index, city] = value

# Splitting previous DATETIME column into DATE and TIME
# Dropping DATETIME column
# Converting DATE column into DATE format to enable sorting with groupby function
df[['DATE', 'TIME']] = df['DATETIME'].str.split(" ", expand=True)
df.drop('DATETIME', inplace=True, axis=1)
df['DATE'] = pd.to_datetime(df['DATE'], dayfirst=True)

# Counting average temperature for each day in each city
df = df.groupby('DATE').mean()

station_weight = {'Brice Norton': 0.14,
                  'Herstmonceux': 0.10,
                  'Heathrow': 0.30,
                  'Nottingham': 0.13,
                  'Shawbury': 0.20,
                  'Waddington': 0.13
                  }

# Counting UK average for each day accounting for weights assigned to each city
df['UK_avg'] = 0
for station in station_weight:
    df['UK_avg'] += df[station] * station_weight[station]

# Result
print(df['UK_avg'])



