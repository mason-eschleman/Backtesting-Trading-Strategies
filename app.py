import pandas as pd

df = pd.read_csv("TQQQ_intraday_data.csv", parse_dates=['Date'], index_col='Date')

df