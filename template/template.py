import dash
from dash import html
import dash_bootstrap_components as dbc
import dash_core_components as dcc    


# 1. Create all of the components you plan to inject into the rows and columns of the layout.

navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Page 1", href="#")),
        dbc.DropdownMenu(
            children=[
                dbc.DropdownMenuItem("More pages", header=True),
                dbc.DropdownMenuItem("Page 2", href="#"),
                dbc.DropdownMenuItem("Page 3", href="#"),
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

badge = dbc.Button(
    [
        "Notifications",
        dbc.Badge("7", color="light", text_color="primary", className="ms-1"),
    ],
    color="primary",
)

jumbotron = html.Div(
    dbc.Container(
        [
            html.H1("Jumbotron", className="display-3"),
            html.P(
                "Use Containers to create a jumbotron to call attention to "
                "featured content or information.",
                className="lead",
            ),
            html.Hr(className="my-2"),
            html.P(
                "Use utility classes for typography and spacing to suit the "
                "larger container."
            ),
            html.P(
                dbc.Button("Learn more", color="primary"), className="lead"
            ),
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

# 3. Start the Dash server
if __name__ == "__main__":
    app.run_server()
