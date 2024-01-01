
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def load_metadata(path):
    if path != "":
        return pd.read_csv(path)
    return None

def show_most_common_emergencies(data):
    # Most common emergencies
    if not data.empty:
        unique_problem_counts = data['avh_problem'].value_counts()
        fig = px.bar(data, 
                     x=unique_problem_counts.index, 
                     y=unique_problem_counts.values, 
                     color=unique_problem_counts.index,
                     title="Most Common Emergencies")
        fig.update_layout(paper_bgcolor='rgba(0,0,0,0)',
                          xaxis_title='Emergency Type',
                          font=dict(color='white'),
                          yaxis_title='Count')
        return fig
    return None

def show_common_emergency_outcome(data):
    if not data.empty:
        unique_problem_counts = data['avh_result'].value_counts()
        fig = px.bar(data, 
                        x=unique_problem_counts.index, 
                        y=unique_problem_counts.values, 
                        color=unique_problem_counts.index,
                        title="Most Common Emergency Outcomes")
        fig.update_layout(paper_bgcolor='rgba(0,0,0,0)',
                          font=dict(color='white'),
                            xaxis_title='Emergency Outcome',
                            yaxis_title='Count')
        return fig
    return None

def show_emergency_count_by_origin_path(data):
    if not data.empty:
        count_by_location = data.groupby('origin')['avh_problem'].count().reset_index()
        fig = px.bar(count_by_location, 
                     x='origin', 
                     y='avh_problem', 
                     color='origin',
                     title="Count of Emergencies By Origin Flight Path (Aviation Herald)")
        fig.update_layout(paper_bgcolor='rgba(0,0,0,0)',
                            xaxis_title='Origin',
                            yaxis_title='Count of Emergency',
                            font=dict(color='white'))
        return fig
    return None

def process_trajectory_data(data, call_sign):
    '''
    Process the trajectory data
    '''
    if not data.empty:
        # Filter data based on call sign
        trajectories = data[data['callsign'] == call_sign]
        # Skip the timestamp data every 60 secs
        trajectories = trajectories.iloc[::60]
        return trajectories
    return None
    
def show_flight_path_map(processed_data, call_sign):
    '''
    Display the flight path map
    '''
    if not processed_data.empty:
        # Create an animated scatter plot using Plotly
        fig = px.scatter_mapbox(processed_data,
                                lat="latitude",
                                lon="longitude",
                                hover_data={"timestamp": "|%B %d, %Y %I:%M %p"},
                                zoom=5,
                                animation_frame="timestamp",
                                mapbox_style="carto-darkmatter",
                                title=f"Flight Path of {call_sign}").update_traces(marker_size=8)

        fig.update_layout(mapbox_center={"lat": processed_data['latitude'].mean(),
                                        "lon": processed_data['longitude'].mean()},
                          plot_bgcolor='rgba(0,0,0,0)',  # Transparent background color
                          paper_bgcolor='rgba(0,0,0,0)',  # Transparent paper color
                          font=dict(color='white'),
                          width=1920,
                          height=800 
        )
        
        # Segregate data between 7700 and nominal
        line_for_7700 = processed_data[processed_data['squawk'] ==  '7700']
        line_nominal = processed_data[processed_data['squawk'] !=  '7700']

        # Create a line trace for 7700
        line_trace_7700 = go.Scattermapbox(
            mode="lines",
            lat=line_for_7700['latitude'],
            lon=line_for_7700['longitude'],
            line=dict(width=1, color='red'),
            name = '7700'
        )

        # Create a line trace for nominal
        line_trace_nominal = go.Scattermapbox(
            mode="lines",
            lat=line_nominal['latitude'],
            lon=line_nominal['longitude'],
            line=dict(width=1, color='green'),
            name='nominal'
        )
        
        # Add the lines to figure
        fig.add_trace(line_trace_7700)
        fig.add_trace(line_trace_nominal)
        
    return fig

    