import dash
import plotly.graph_objects as go
import numpy as np

xa = np.random.randn(500)
xb = np.random.randn(500) + 1

fig2 = go.Figure()
fig2.add_trace(go.Histogram(x=xa))
fig2.add_trace(go.Histogram(x=xb))

# The two histograms are drawn on top of another
fig2.update_layout(barmode='stack')