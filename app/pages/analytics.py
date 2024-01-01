import dash_bootstrap_components as dbc
from utils import data_processor
from dash import html, dcc

def analytics_page(metadata_path):
    metadata = data_processor.load_metadata(metadata_path)
    most_common_emergencies_fig = data_processor.show_most_common_emergencies(metadata)
    most_common_emergency_outcome_fig = data_processor.show_common_emergency_outcome(metadata)
    count_emergency_by_origin_fig = data_processor.show_emergency_count_by_origin_path(metadata)
    
    return html.Div([
        html.Div([
            dbc.Row(
            [
                dbc.Col(html.Div(
                    dcc.Graph(
                            id='common-emergency-graph', 
                            figure=most_common_emergencies_fig)
                    )),
                dbc.Col(html.Div(
                    dcc.Graph(
                            id='common-emergency-outcome-graph', 
                            figure=most_common_emergency_outcome_fig)
                    )),
                dbc.Col(html.Div(
                    dcc.Graph(
                            id='count-emergency-by-origin-graph', 
                            figure=count_emergency_by_origin_fig)
                    )),
            ]
        )
        ], className='analytics-inner-div')
        ], className='analytics-div')