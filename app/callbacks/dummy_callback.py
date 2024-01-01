from app.app import app  # Import the Dash app instance
from dash.dependencies import Input, Output

# Define a callback function
@app.callback(
    Output('output-div', 'children'),
    [Input('input', 'value')]
)
def update_output(value):
    return f'You entered: {value}'