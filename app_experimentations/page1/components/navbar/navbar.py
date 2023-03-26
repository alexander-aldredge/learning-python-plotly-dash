#!/usr/bin/python

import dash_bootstrap_components as dbc


# This is the code for a navbar.
navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(
            dbc.NavLink(
                "USA Patient Data",
                href="#",
            ),
        ),
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