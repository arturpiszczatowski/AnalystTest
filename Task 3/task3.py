import os
import numpy as np
import pandas as pd


df_temp = pd.read_csv(os.path.abspath('Task 3/TemperaturesNorthCarolina.csv'), encoding='unicode_escape')
df_gas = pd.read_csv(os.path.abspath('Task 3/GasPowerDemandNorthCarolina.csv'), encoding='unicode_escape')

# removing empty columns
df_gas = df_gas.drop(df_gas.iloc[:, 2:], axis=1)

# temperatures for which gas power demand will be forecasted
df_search = df_temp.iloc[len(df_gas):, :]

# temperatures for which gas power demand is known
df_temp = df_temp.iloc[:len(df_gas), :]
df = pd.merge(df_temp, df_gas, on='DATES')
df.drop('DATES', axis=1, inplace=True)

# generalization of recorded temperature
df[df.columns[0]] = df[df.columns[0]].apply(np.ceil)

# average G2P for each temperature recorded
df = df.groupby(df.columns[0], as_index=False).mean()

# assigning mean G2P to respective temperatures
df_search[df_search.columns[1]] = df_search[df_search.columns[1]].apply(np.ceil)
df_search = pd.merge(df_search, df, on=df_search.columns[1], how='left')

# forecasted g2p for 7/1/2020-9/30/2020 period
print(df_search[[df_search.columns[0], df_search.columns[2]]].to_string())
