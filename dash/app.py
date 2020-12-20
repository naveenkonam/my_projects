import dash
import dash_core_components as dcc
import dash_html_components as dhl

import plotly.express as px
import pandas as pd

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgp.css']
app = dash.Dash(__name__,external_stylesheets=external_stylesheets)

df = pd.DataFrame({"Fruit":["Apples","Oranges"],"Amount":[4,1]})

fig = px.bar(df, x = "Fruit", y = "Amount")

app.layout= dhl.Div(children=[dhl.H1(children='Hello Dash'),
    dcc.Graph(id = 'example',figure = fig)])

if __name__ ==  '__main__':
    app.run_server(debug=True)
