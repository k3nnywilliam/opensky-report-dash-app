import dash_bootstrap_components as dbc
from dash import html

def flight_learn_page():
    return html.Div([
        dbc.Row(
            [
                dbc.Col(html.Div("Graph 1")),
                dbc.Col(html.Div("Graph 2")),
                dbc.Col(html.Div("Graph 3")),
            ]
        )
        ], className='learn-div')