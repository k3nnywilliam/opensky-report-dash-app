from app import app
from dash import html
from dash import Input, Output, State
from pages import home, analytics, flight_paths

def render_page_callback(app):
    