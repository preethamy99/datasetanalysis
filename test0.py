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
