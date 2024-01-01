# user_input_callbacks.py

from dash.dependencies import Input, Output
from app import app  # Assuming 'app' is the Dash app object

# Define your callback functions
@app.callback(
    Output('output-div', 'children'),
    [Input('input-field', 'value')]
)
def update_output(value):
    processed_data = "processed"
    return f"Processed data: {processed_data}"
