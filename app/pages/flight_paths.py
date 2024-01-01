from dash import dcc, html
import dash_bootstrap_components as dbc
import pandas as pd
from utils import data_processor
import os
import logging

def flight_paths_page(data_path, call_sign):
    logging.info(f'Reading the trajectory data...')
    flight_data = pd.read_parquet(data_path, engine='pyarrow')
    #flight_data = pd.DataFrame()
    if not flight_data.empty:
        logging.info(f'Processing the trajectory data...')
        processed_data1 = data_processor.process_trajectory_data(flight_data, 'UAL342')
        processed_data2 = data_processor.process_trajectory_data(flight_data, 'BAW119')
        processed_data3 = data_processor.process_trajectory_data(flight_data, 'BAW79J')
        logging.info(f'Displaying the flight trajectory...')
        fig1 = data_processor.show_flight_path_map(processed_data1, 'UAL342')
        fig2 = data_processor.show_flight_path_map(processed_data2, 'BAW119')
        fig3 = data_processor.show_flight_path_map(processed_data3, 'BAW79J')
        return html.Div([
            html.Div([
                dbc.Row(
                    dcc.Graph(
                    id='flight-map-1', 
                    figure=fig1)),
                dbc.Row(
                    dcc.Graph(
                    id='flight-map-2', 
                    figure=fig2)),
                dbc.Row(
                    dcc.Graph(
                    id='flight-map-3', 
                    figure=fig3)),
                ], className='flight-path-inner-div')
            ], className='flight-path-div')
    else:
        logging.warning(f'Flight data is empty!')
        return html.Div([
            html.Div([])
            ], className='flight-path-div')