
import dash
import os
import dash_bootstrap_components as dbc
from dash import Input, Output, State, dcc, html
from pages import home, analytics, flight_paths, learn
from components.navbar import navbar_component
from components.footer import foot

app = dash.Dash(
    external_stylesheets=[dbc.themes.SUPERHERO, 'https://cdnjs.cloudflare.com/ajax/libs/animate.css/4.1.1/animate.min.css'],
    # these meta_tags ensure content is scaled correctly on different devices
    # see: https://www.w3schools.com/css/css_rwd_viewport.asp for more
    meta_tags=[
        {"name": "viewport", "content": "width=device-width, initial-scale=1"}
    ],
)

# Change the title of the browser tab
app.title = 'OpenSky Report'
# Change the favicon
app._favicon = "flight_plane.ico"
# Default page content
content = html.Div(id="page-content")

# Set app layout
app.layout = html.Div([
    dcc.Location(id="url"), 
    html.Script(src='assets/custom_scroll.js'),
    navbar_component(), 
    content])


@app.callback(
    Output("page-content", "children"), 
    [Input("url", "pathname")],
    prevent_initial_call=True)
def render_page_content(pathname):
    if pathname == "/":
        return home.display_homepage()
    elif pathname == "/analytics":
        return analytics.analytics_page(metadata_path="app/assets/data/metadata_cleaned.csv")
    elif pathname == "/flight_paths":
        return flight_paths.flight_paths_page(data_path=f'app/assets/data/trajectories_cleaned.parquet', call_sign='UAL342')
    elif pathname == "/learn":
        return learn.flight_learn_page()
    # If the user tries to reach a different page, return a 404 message
    return html.Div(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ],
        className="p-3 bg-light rounded-3",
    )
    


if __name__ == "__main__":
    app.run_server(port=8888, debug=True)