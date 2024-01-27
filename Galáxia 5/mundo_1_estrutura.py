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

app = Dash(__name__)
