import dash_bootstrap_components as dbc
from dash import Dash, html, dcc, dash_table, callback

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = dbc.Container([

    dbc.Row([

        dbc.Col(html.P('Nossa primeira coluna'), width=2, style={'background-color':'green'}),

        dbc.Col(html.P('Nossa segunda coluna'), width=2, style={'background-color':'blue'}),

        dbc.Col(html.P('Nossa terceira coluna'), width=8, style={'background-color':'yellow'}),

    ],

    style={'height':'400px'}

    ),

    dbc.Row([

        dbc.Col(html.P('Nossa primeira coluna da segunda linha'), style={'background-color':'red'}),

        dbc.Col(html.P('Nossa segunda coluna da segunda linha'), style={'background-color':'orange'}),

    ]),

    dbc.Row([

        dbc.Col(html.P('Teste'), width=8, style={'color':'black'}),

        dbc.Col([

            dbc.Row([

                dbc.Col(html.P('Estamos dentro de várias linhas'), width=4, style={'background-color':'purple'}),

                dbc.Col(html.P('Estamos dentro de várias linhas'), width=6, style={'background-color':'red'}),

            ])

        ], width=4, style={'background-color':'green'}),

    ]),

],

style={'max-width':'100%', 'color':'white'}

)


if __name__ == '__main__':
    app.run_server(debug=True)