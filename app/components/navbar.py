import dash_bootstrap_components as dbc

def navbar_component():
    navbar = dbc.NavbarSimple(
    children=[
        dbc.Nav([
            dbc.NavItem(dbc.NavLink("Home", href="/")),
            dbc.NavItem(dbc.NavLink("Analytics", href="/analytics")),
            dbc.NavItem(dbc.NavLink("Flight Paths", href="/flight_paths")),
            dbc.NavItem(dbc.NavLink("Learn", href="/learn")),
    ], style={'padding': '10px'}, id='scroll-comp')
    ],
    brand="OpenSky Report",
    brand_href="https://opensky-network.org/",
    color="Light",
    dark=True,
    style={'position': 'fixed', 'fontSize': 'x-large', 'marginLeft': '30px', 'marginRight': '30px', 'top': '0', 'background': 'transparent'},
    )
    
    return navbar