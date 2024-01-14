#!/usr/bin/python

# Import Essential libraries for Dash dashboard.
import dash
from dash import dcc
from dash import html
import dash_bootstrap_components as dbc
from plots import fig1, fig2, fig3, fig4

# Define the layout of the app.
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
app.layout = dbc.Container([

    # Row 1.
    dbc.Row([
        dbc.Col([
            html.H1("Patients By Age:"), 
            dcc.Graph(figure = fig1),
        ],
            width = 6,
        ),

        dbc.Col([
            html.H1("Race:"),
            dcc.Graph(figure = fig3),
        ],
            width = 3,
        ),

        dbc.Col([
            html.H1("Gender:"),
            dcc.Graph(figure = fig3),
        ],
            width = 3,
        )
    ]),

    # Row 2.
    dbc.Row([
        dbc.Col([
            html.H1("Patients Over Time:"),
            dcc.Graph(figure = fig2),
        ],
          width = 6,
        ),

        dbc.Col([
            html.H1("COVID-19:"),
            dcc.Graph(figure = fig3),
        ],
           width = 3,
        ),
        dbc.Col([
            html.H1("Survived / Deceased:"),
            dcc.Graph(figure = fig3),
        ],
            width = 3,
        )
    ]),

    # Row 3.
    dbc.Row([
        dbc.Col([
            html.H1("Map Of Survival:"),
            dcc.Graph(figure = fig4),
        ],
            width = 6,
        ),

        dbc.Col([
            html.H1("Map Of Death:"),
            dcc.Graph(figure = fig4),
        ],
            width = 6,
        )
    ]),

],

fluid = True,
style={"padding": "0"},
)

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
