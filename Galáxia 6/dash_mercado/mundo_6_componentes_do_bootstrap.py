from dash import Dash, html, dcc, callback, Output, Input, dash_table
import dash_bootstrap_components as dbc
from mundo_5_dados import dados_cotacoes, grafico_candle, grafico_inflacao
from dash_bootstrap_templates import load_figure_template

load_figure_template('darkly')

cotacoes, tikers = dados_cotacoes()
fig_candle = grafico_candle(tikers)

app = Dash(__name__, external_stylesheets=[dbc.themes.DARKLY])

app.layout = dbc.Container(
    [

    dbc.Row(
    
        [
            
            dbc.Col(

                [

                    dbc.Row(
                        [
                            dbc.Col(width=2),
                            dbc.Col(html.H1(children='Tabela de Cotações', className='titulos-do-dash'), width=8),
                            dbc.Col(width=2) 
                        ]),

                    dbc.Row(children=dash_table.DataTable(cotacoes.to_dict('records'), id='tabela_teste',
                                                          style_header={
                                                            'backgroundColor':'#333E66',
                                                            'fontWeight':'bold',
                                                            'border':'0px',
                                                            'font-size':'12px',
                                                            'color':'#D3D6DF',
                                                            'borderRadius':'8px',
                                                          },
                                                          style_cell={
                                                              'textAlign':'center',
                                                              'padding':'4px 4px',
                                                              'backgroundColor':'#212946',
                                                              'borderRadius':'8px',
                                                              'color':'#D3D6DF',
                                                          },
                                                          style_data={
                                                              'border':'8px',
                                                              'font-size':'12px',
                                                          },
                                                          style_table={
                                                              'borderRadius':'8px',
                                                              'overflow':'hidden',
                                                          },
                                                          style_data_conditional=
                                                          [
                                                              {
                                                                  'if':{
                                                                      'filter_query':'{Preço} > 20',
                                                                      'column_id':'Preço'
                                                                  },
                                                                  'color':'#19C819'
                                                              },
                                                              {
                                                                  'if':{
                                                                      'filter_query': '{Preço} < 20',
                                                                      'column_id':'Preço'
                                                                  },
                                                                  'color':'#E50000'
                                                              }
                                                          ]
                            )),

                ], 

                style={'margin':'8px'}

            ),
            
            dbc.Col(

                [

                    dbc.Row(
                        [
                            dbc.Col(width=2),
                            dbc.Col(html.H1(children='Gráfico de Candle', className='titulos-do-dash'), width=8),
                            dbc.Col(width=2)
                        ]
                    ),

                    dbc.Row(children=dcc.Graph(figure=fig_candle, style={'height':'400px'})),

                ], 

                style={'margin':'8px'}

            )
        
        ], 
        
        style={'height':'50vh', 'padding':'12px'}
    
    ),

    dbc.Row(
    
        [
            
            dbc.Col(children=
                    [
                        dbc.Row(
                            [
                                dbc.Col(dbc.Button('Botão Primário', color='primary'), style={'display':'flex', 'justify-content':'center'}),
                                dbc.Col(dbc.Button('Botão Secundário', color='secondary'), style={'display':'flex', 'justify-content':'center'})
                            ]
                        ),
                        dbc.Row(dbc.Card(
                            [
                                dbc.CardImg(src='/assets/petrobras.png', top=True),
                                dbc.CardBody(
                                    [
                                        html.H4('Título do Card', className='card-title'),
                                        html.P('Sinta-se a vontade de criar o seu próprio card.', className='card-text'),
                                        dbc.Button('Ação do card', color='primary'),
                                    ]
                                ),
                            ], 
                            style={'width':'18em'},
                        ), 
                        style={'display':'flex', 'justify-content':'center', 'margin-top':'12px'}
                        )
                    ]
            ),
            
            dbc.Col(

                [

                    dbc.Row(
                        [
                            dbc.Col(width=2),
                            dbc.Col(html.H1(children='Gráfico de Inflação', className='titulos-do-dash'), width=8),
                            dbc.Col(width=2)
                        ]
                    ),

                    dbc.Row(
                        
                        [
                            dbc.Col(dcc.Dropdown(['IPCA', 'IGP-M'], 'IPCA', id='drop_infla_callback',
                                                 style={'background-color':'black', 'color':'white'}), width=3),
                            dbc.Col(dcc.Dropdown(['6', '12', '24'], '6', id='drop_infla_callback_periodo',
                                                 style={'background-color':'black', 'color':'white'}), width=3)
                        ]
                    ),

                    dbc.Row(children=dcc.Graph(id='grafico_com_callback')),

                ],

                style={'margin':'8px'}

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
