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
import graph3
# import graph4
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
        dbc.Row([
        dbc.Col(
            html.H1("Patients By Age:"),
            width = 6,
        ),

        dbc.Col(
           html.H1("Race:"),
           width = 3,
        ),

        dbc.Col(
            html.H1("Gender:"),
            width = 3
        )
    ]),
]),
        dbc.Row([
        dbc.Col(
            dcc.Graph(figure = graph1.fig1),
            width = 6,
        ),

        dbc.Col(
            dcc.Graph(figure = graph3.fig3),
            width = 3
        ),

        dbc.Col(
            dcc.Graph(figure = graph3.fig3),
            width = 3
        )
    ]),


    dbc.Row([
            dbc.Row([
            dbc.Col(
                html.H1("Patients Over Time:"),
                width = 6,
            ),

            dbc.Col(
            html.H1("COVID-19:"),
            width = 3,
            ),

            dbc.Col(
                html.H1("Survived / Deceased:"),
                width = 3,
            )
        ]),
    ]),

    dbc.Row([
        dbc.Col(
            dcc.Graph(figure = graph2.fig2),
            width = 6
        ),

        dbc.Col(
            dcc.Graph(figure = graph3.fig3),
            width = 3
        ),
        dbc.Col(
            dcc.Graph(figure = graph3.fig3),
            width = 3
        )
    ]),

    dbc.Row([
        dbc.Col(
                html.H1("Map Of Survival:"),
            width = 6
        ),

        dbc.Col(
                html.H1("Map Of Death:"),
            width = 6
        )
    ]),

    dbc.Row([
        dbc.Col(
            dcc.Graph(figure = graph1.fig1),
            width = 6
        ),

        dbc.Col(
            dcc.Graph(figure = graph1.fig1),
            width = 6
        )
    ]),

],
fluid=True,
)


# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)