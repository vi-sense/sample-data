#!/usr/bin/env python3
import pandas as pd
import plotly.express as px

df = pd.read_csv('cape-town/return_flow_temperature.csv')
fig = px.line(df, x = 'date', y = 'value', title='test')
fig.show()

