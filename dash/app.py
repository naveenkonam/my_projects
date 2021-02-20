import dash
import dash_core_components as dcc
import dash_html_components as dhl

import plotly.express as px
import pandas as pd

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgp.css']
app = dash.Dash(__name__,external_stylesheets=external_stylesheets)

df = pd.read_excel(r"/home/konam/Desktop/RCC.xlsx")

fig = px.bar(df, x = "Date", y = "RCC")
#fig1 = px.bar(df, x = "Date", y = "Fab")

app.layout= dhl.Div(children=[dhl.H1(children='RCC'),
    dcc.Graph(id = 'RCC',figure = fig)])

#app.layout=dhl.Div(children=[dhl.H1(children='Fab'),
 #   dcc.Graph(id='Fab',figure = fig1)])

if __name__ ==  '__main__':
    app.run_server(debug=True)
