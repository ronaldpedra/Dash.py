from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd
from mundo_1_import import *

'''
DADOS
APP
LAYOUT
CALLBACKS
RODAR O APP
'''

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder_unfiltered.csv')

app = Dash(__name__) # Esse é o nome do seu código

app.layout = html.Div([
  html.H1(children='Title of Dash App', style={'textAlign':'center'}),
  dcc.Dropdown(df.country.unique(), 'Canada', id='dropdown-selection'),
  dcc.Graph(id='graph-content')
])
