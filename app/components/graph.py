from dash import dcc

def GraphComponent():
    return dcc.Graph(id='example-graph', figure={'data': [{'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'Example'}]})