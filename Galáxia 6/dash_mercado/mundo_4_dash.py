from dash import Dash, html, dcc, callback, Output, Input, dash_table
import dash_bootstrap_components as dbc
from mundo_4_isolando_coleta_de_dados import dados_cotacoes, grafico_candle, grafico_inflacao

cotacoes, tikers = dados_cotacoes()
fig_candle = grafico_candle(tikers)

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = dbc.Container(
    [

    dbc.Row(
    
        [
            
            dbc.Col(

                [

                    dbc.Row(children=html.H1(children='Cotações de Ontem'), 
                            style={'display':'flex', 'justify-content':'center'}),

                    dbc.Row(children=dash_table.DataTable(cotacoes.to_dict('records'), id='tabela_teste')),

                ], 

                style={'margin':'8px'}

            ),
            
            dbc.Col(

                [

                    dbc.Row(children=html.H1(children='Gráfico de Candle'), 
                            style={'display':'flex', 'justify-content':'center'}),

                    dbc.Row(children=dcc.Graph(figure=fig_candle, style={'height':'400px'})),

                ], 

                style={'margin':'8px'}

            )
        
        ], 
        
        style={'height':'50vh'}
    
    ),

    dbc.Row(
    
        [
            
            dbc.Col(children=
                    
                    [

                        html.P('Elementos do Dash'),
                        dcc.Dropdown(['IPCA', 'IGP-M'], 'IPCA', id='escolher_inflacao', multi=True),
                        html.Br(),
                        dcc.Checklist(['IPCA', 'IGP-M'], id='checklist-padrao'),
                        html.Br(),
                        dcc.Slider(0, 30, 5)
                        
                    ], 
                    
                    style={'margin':'8px'}),
            
            dbc.Col(

                [

                    dbc.Row(children=html.H1(children='Gráfico de Inflação'), 
                            style={'display':'flex', 'justify-content':'center'}),

                    dbc.Row(
                        
                        [
                            dcc.Dropdown(['IPCA', 'IGP-M'], 'IPCA', id='drop_infla_callback'),
                            dcc.Dropdown(['6', '12', '24'], '6', id='drop_infla_callback_periodo')
                        ]
                    ),

                    dbc.Row(children=dcc.Graph(id='grafico_com_callback')),

                ]

            )
    
        ], 
        
        style={'height':'50vh'}
    
    )
    
    ], 
    
    style={'max-width':'100%'}
    
)

@app.callback(
    Output('grafico_com_callback', 'figure'),
    Input('drop_infla_callback', 'value'),
    Input('drop_infla_callback_periodo', 'value')
)
def criando_grafico_infla(valor_do_dropdown_indicador, valor_do_dropdown_periodo):

    fig_inflacao = grafico_inflacao(valor_do_dropdown_indicador, valor_do_dropdown_periodo)
    
    return fig_inflacao


if __name__ == '__main__':
    app.run(debug=True, port=8050)
