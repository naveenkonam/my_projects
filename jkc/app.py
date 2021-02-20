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
             dbc.Col(html.Div(html.H2("JK Cements Limited")),width=9)
             ]),
         
         dbc.NavbarSimple([
             dbc.NavItem(dbc.NavLink("Home",href = "#")),
             dbc.NavItem(dbc.NavLink("Ordering",href = "#")),
             dbc.NavItem(dbc.NavLink("Delivery",href = "#")),
             dbc.NavItem(dbc.NavLink("Construction",href = "#"))],
             
             brand = 'Project DashBoard',
             brand_href = "#",
             color = 'primary',
             dark = True,
             ),                
        
         dbc.Row([
             dbc.Col(html.Div(dcc.Graph(id='scurve',figure=fig4)),width={"size":6,"order":1}),
             dbc.Col(html.Div(dcc.Graph(id='cost',figure=fig3)),width={"size":6,"order":2})
             ]),
        
         dbc.Row([
             dbc.Col(html.Div(dcc.Graph(id='rcc',figure=fig1)),width=4),
             dbc.Col(html.Div(dcc.Graph(id='fab',figure=fig2)),width=4)
            ]),
        ])
        
if __name__ == '__main__':
    app.run_server(debug=True)
