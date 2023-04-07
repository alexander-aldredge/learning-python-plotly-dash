#!/usr/bin/python

import dash
import plotly.graph_objects as go
import numpy as np

x0 = np.random.randn(500)
x1 = np.random.randn(500) + 1

fig1 = go.Figure()
fig1.add_trace(go.Histogram(x=x0))
fig1.add_trace(go.Histogram(x=x1))

# Overlay both histograms
fig1.update_layout(barmode='overlay')
fig1.update_traces(name='name1', selector=dict(type='histogram'))

# Reduce opacity to see both histograms
fig1.update_traces(opacity=0.80)
