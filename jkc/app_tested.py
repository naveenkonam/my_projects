# test app for dash app

import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd

external_stylesheets = [dbc.themes.BOOTSTRAP]
df1 = pd.read_excel("/home/konam/Desktop/RCC.xlsx",'cons')
df2 = pd.read_excel("/home/konam/Desktop/RCC.xlsx",'cost')
df3 = pd.read_excel("/home/konam/Desktop/RCC.xlsx",'scurve')
df4 = pd.read_excel("/home/konam/Desktop/RCC.xlsx",'manpower')

fig1 = px.bar(df1, x="Month", y="RCC", title = "RCC Graph")
fig2 = px.bar(df1, x="Month", y="Fab", title = "Fab Graph")
fig3 = px.line(df2,x="month",y="variance",title = "Cost variance")
fig4 = px.line(df3,x = "Month", y=df3.columns, title = "S Curve")
fig5 = px.bar(df4, x = "Department",y=df4.columns, title = "Man Power", barmode = 'group')

app = dash.Dash(__name__,external_stylesheets = external_stylesheets)

app.layout= html.Div([
         dbc.Row([
             dbc.Col(html.Div(html.H2("JK Cements Limited")),width=9),
             dbc.Col(html.Div(html.H2("Project DashBoard")),width=9),
             ]),
         dbc.Row([html.Div(dcc.Graph(id='curve',figure=fig1))])               
        ])
        
        
        

if __name__ == '__main__':
    app.run_server(debug=True)
