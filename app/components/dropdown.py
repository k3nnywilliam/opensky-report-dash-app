from dash import dcc

def DropdownComponent():
    return dcc.Dropdown(options=[{'label': i, 'value': i} for i in ['A', 'B', 'C']], value='')
