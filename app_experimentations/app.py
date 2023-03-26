import dash
from dash import dcc
from dash import html
import plotly.express as px

import sys
sys.path.insert(0, './page1/components/body/graphs')
sys.path.insert(0, './page2/components/body/graphs')

import graph1
import graph2

# Load a sample dataset
data = px.data.tips()

# Define the layout of the app
app = dash.Dash(__name__)
app.layout = html.Div([

    html.Div([
        dcc.Graph(
            figure = graph1.fig1
        )
    ]),

    html.Div([
        dcc.Graph(
            figure = graph2.fig2
        )
    ])
])

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)