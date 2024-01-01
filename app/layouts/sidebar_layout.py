# sidebar_layout.py

from dash import Input, Output, State, html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

def create_sidebar():
    sidebar = html.Div(
    [
        dbc.Button(
            "Open collapse",
            id="horizontal-collapse-button",
            className="mb-3",
            color="primary",
            n_clicks=0,
        ),
        html.Div(
            dbc.Collapse(
                dbc.Card(
                    dbc.CardBody(
                        "This content appeared horizontally due to the "
                        "`dimension` attribute"
                    ),
                    style={"width": "400px"},
                ),
                id="horizontal-collapse",
                is_open=False,
                dimension="width",
            ),
            style={"minHeight": "100px"},
        ),
    ]
)
    return sidebar


