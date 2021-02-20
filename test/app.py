import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
 
"""Importing the css stylesheet"""
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css'] 

"""Initializing the app"""
app = dash.Dash(__name__, external_stylesheets = external_stylesheets)
 
app.layout = html.Div([html.H1("This is test Dash App")])
 
if __name__ == '__main__':
    app.run_server(debug = True)

