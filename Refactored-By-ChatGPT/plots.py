#!/usr/bin/python
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
from urllib.request import urlopen
import json

# Plot 1
x0 = np.random.randn(5000)
x1 = np.random.randn(5000) + 1
fig1 = go.Figure()
fig1.add_trace(go.Histogram(x=x0))
fig1.add_trace(go.Histogram(x=x1))
fig1.update_layout(barmode='overlay')
fig1.update_traces(opacity=0.80)

# Plot 2
xa = np.random.randn(500)
xb = np.random.randn(500) + 1
fig2 = go.Figure()
fig2.add_trace(go.Histogram(x=xa))
fig2.add_trace(go.Histogram(x=xb))
fig2.update_layout(barmode='stack')

# Plot 3
df = pd.read_csv('../patient-data/Dataset.csv')
df1 = df.loc[df['gender'].isin(['M', 'F'])]
gender_counts = df1.groupby('gender').count().reset_index()
fig3 = px.pie(gender_counts, values='encounter_id', names='gender', hole=.3)

# Plot 4
with urlopen('https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json') as response:
    counties = json.load(response)
df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/fips-unemp-16.csv", dtype={"fips": str})
fig4 = px.choropleth_mapbox(df, geojson=counties, locations='fips', color='unemp', color_continuous_scale="Viridis", range_color=(0, 12), mapbox_style="carto-positron", zoom=3, center = {"lat": 37.0902, "lon": -95.7129}, opacity=0.5, labels={'unemp':'unemployment rate'})
fig4.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
