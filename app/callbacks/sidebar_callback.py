from app import app
from dash import html
from dash.dependencies import Input, Output, State

# Define callback function for sidebar toggle
def toggle_sidebar_callback(app):
    @app.callback(
        Output("horizontal-collapse", "is_open"),
        [Input("horizontal-collapse-button", "n_clicks")],
        [State("horizontal-collapse", "is_open")],
    )
    def toggle_collapse(n, is_open):
        if n:
            return not is_open
        return is_open
