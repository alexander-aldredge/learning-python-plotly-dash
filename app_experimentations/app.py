#!/usr/bin/python

# Import Essential libraries for Dash dashboard.
import dash
from dash import dcc
from dash import html
import dash_bootstrap_components as dbc
import plotly.express as px

# Import the files from other repositories containing the graphs to be used in the dashobard.
import sys
sys.path.insert(0, './page1/components/body/graphs')
import graph1
import graph2
# sys.path.insert(0, './page2/components/body/graphs')
sys.path.insert(0, './page1/components/navbar')
from navbar import navbar

# Load a sample dataset.
data = px.data.tips()

# Define the layout of the app.
# This will be the HTML & Boostrap front end.
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
app.layout = dbc.Container([

    navbar,

    dbc.Row([
        dbc.Col(
            dcc.Graph(
                figure = graph1.fig1
            )
        ),

        dbc.Col(
            dcc.Graph(
                figure = graph1.fig1
            )
        )
    ]),

    dbc.Row([
        dbc.Col(
            dcc.Graph(
                figure = graph2.fig2
            )
        ),

        dbc.Col(
            dcc.Graph(
                figure = graph2.fig2
            )
        )
    ])
],
fluid=True,
)


# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)