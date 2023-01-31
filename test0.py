import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
w_df = pd.read_csv(r"E:\documents\Downloads\1. Weather Data.csv")
w_df.shape()
w_df.head()
w_df.columns
w_df.index
w_df.dtype
w_df[].unique()
w_df[].nunique() or w_df.nunique()
w_df.count
w_df.info()
# visulizing the data
fig = plt.scatter(w_df['Temp_C'],w_df['Rel Hum_%'])
fig
# pressure distribution 
sns.displot(w_df['Press_kPa'], kde = True)
# distribution of columns
for i in w_df.column:
  sns.displot(w_df[i], kde = True)
#filter data
w_df[w_df['Temp_C'] < 0]
# filter based on different conditions
w_df[(w_df['Weather'] == 'snow') & (w_df['Wind Speed_km/h'] > 40)]
#checking is there ny null vlues in the data 
w_df.isnull().sum()
