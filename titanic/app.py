import dash
from dash import html
from dash import dcc
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px


# load data
# Data came from < https://www.kaggle.com/c/titanic/data?select=train.csv >
df = pd.read_csv('train.csv')


# initialize app
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.UNITED])


# set app layout
app.layout = html.Div(children=[

    html.H1('Test Dash App', style={'textAlign': 'center'}),
    html.Br(),

    dcc.Dropdown(
        options=[{'label': i, 'value': i} for i in df.columns],
        value='Age',
        id='dropdown',
        style={"width": "50%", "offset": 1},
        clearable=False,
    ),

    dcc.Graph(id='histogram')

])


# callbacks
@app.callback(
    Output(component_id='histogram', component_property='figure'),
    Input (component_id='dropdown',  component_property='value'),
)
def update_hist(feature):
    fig = px.histogram(df, x=feature)
    return fig


if __name__ == "__main__":
    app.run_server(debug=True)
