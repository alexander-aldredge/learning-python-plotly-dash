#!/usr/bin/python

import plotly.express as px

df = px.data.tips()
fig3 = px.pie(df, values='tip', names='day')