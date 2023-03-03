import dash
from dash import html, dcc
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd


# 0. Provide this file with a DataFrame such as through a CSV or through pandas for graphing.
df = pd.DataFrame(dict(
    x = [1, 3, 2, 4],
    y = [1, 2, 3, 4]
))

# 1. Create all of the components you plan to inject into the rows and columns of the layout.

# This is the code for a navbar.
navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("USA Patient Data", href="#")),
        dbc.DropdownMenu(
            children=[
                dbc.DropdownMenuItem("More pages", header=True),
                dbc.DropdownMenuItem("USA Hospital Data", href="#"),
                dbc.DropdownMenuItem("USA Doctor Data", href="#"),
                dbc.DropdownMenuItem("USA Country Data", href="#"),
                dbc.DropdownMenuItem("Canada Country Data", href="#"),
                dbc.DropdownMenuItem("Japan Country Data", href="#"),
            ],
            nav=True,
            in_navbar=True,
            label="More",
        ),
    ],
    brand="Alex's American EMR & Hospital Dashboard",
    brand_href="#",
    color="primary",
    dark=True,
)

df = df.sort_values(by="x")
fig = px.line(df, x="x", y="y", title="Sorted Input")


# This is the code for a jumbotron.
jumbotron = html.Div(
    dbc.Container(
        [
            dcc.Graph(id="histogram")
        ],
        fluid=True,
        className="py-3",
    ),
    className="p-3 bg-light rounded-3",
)


# 2. Create the web-app's front end template and inject the components into the template.
front_end = html.Div(
    [

        # Navbar - This first row is for a navbar that should hold a dropdown that hold the master controlls for the dashboard.
        dbc.Row(dbc.Col(html.Div(navbar), width=12)),

        html.Br(),

        # Row 1 of graphs.
        dbc.Row(
            [
                dbc.Col(html.Div(jumbotron), width=6),
                dbc.Col(html.Div(jumbotron), width=6)
            ],
        ),

        html.Br(),
        
        # Row 2 of graphs.
        dbc.Row(
            [
                dbc.Col(html.Div(jumbotron), width=6),
                dbc.Col(html.Div(jumbotron), width=6)
            ],
        ),

        html.Br(),
        
        # Row 3 of graphs.
        # dbc.Row(
        #     [
        #         dbc.Col(html.Div(jumbotron), width=6),
        #         dbc.Col(html.Div(jumbotron), width=6)
        #     ],
        # ),
        
    ] # End of Front end array.
)



dcc.Input(id ='input',
              value ='Enter a number',
              type ='text'),
html.Div(id ='output')



# 1. Create a Dash app instance
app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])



# 2. Add the example to the app's layout
# First we copy the snippet from the docs
# Then we incorporate the snippet into our layout.
# This example keeps it simple and just wraps it in a Container
# Just inject the template's components into the < dbc.container >'s first paramater as parts of an array.
app.layout = dbc.Container([front_end], fluid=True)



# callbacks
@app.callback(
    Output(component_id='histogram', component_property='figure'),
    Input(component_id='dropdown', component_property='value'),
)
def update_hist(feature):
    fig = px.histogram(df, x=feature)
    return fig



# 3. Start the Dash server
if __name__ == "__main__":
    app.run_server(debug=False)
