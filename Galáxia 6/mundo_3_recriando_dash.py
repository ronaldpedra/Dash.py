from dash import Dash, html, dcc, callback, Output, Input, dash_table
import dash_bootstrap_components as dbc
import yfinance as yf
import datetime
import plotly.graph_objects as go
from bcb import sgs

ticker = ['WEGE3', 'PETR4', 'ABEV3', 'VALE3', 'MGLU3', 'PCAR3', 'ITUB4', 'BBDC4', 'BBAS3']
ticker_yahoo = [ticker + '.SA' for ticker in ticker]

cotacoes = yf.download(ticker_yahoo, start=(datetime.date.today() - datetime.timedelta(days=5)))
cotacoes = cotacoes['Close']
cotacoes = cotacoes.iloc[-1, :]
cotacoes = cotacoes.to_frame()
cotacoes = cotacoes.reset_index()
cotacoes.columns = ['Ticker', 'Preço']
cotacoes['Ticker'] = sorted(ticker)
cotacoes['Preço'] = cotacoes['Preço'].astype(float).round(2)

cotacoes_candle = yf.download(ticker_yahoo[0], start=(datetime.date.today() - datetime.timedelta(days=5)))

layout = go.Layout(yaxis=dict(tickfont=dict(color='#D3D6DF'), showline=False),
                   xaxis=dict(tickfont=dict(color='#D3D6DF'), showline=False))

fig_candle = go.Figure(data=[go.Candlestick(x=cotacoes_candle.index,
                                            open=cotacoes_candle['Open'],
                                            high=cotacoes_candle['High'],
                                            low=cotacoes_candle['Low'],
                                            close=cotacoes_candle['Close']),
                                            ], layout=layout)

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
    
    dados_inflacao = sgs.get({'ipca':433, 'igp-m':189})
    dados_inflacao = dados_inflacao.dropna()
    dados_inflacao = dados_inflacao / 100
    dados_inflacao = dados_inflacao.iloc[-(int(valor_do_dropdown_periodo)):, :]

    if valor_do_dropdown_indicador == 'IPCA':
        dados_inflacao = dados_inflacao['ipca']
        
    elif valor_do_dropdown_indicador == 'IGP-M':
        dados_inflacao = dados_inflacao['igp-m']
    
    layout = go.Layout(yaxis=dict(tickformat='.1%', tickfont=dict(color='black')),
                       xaxis=dict(tickfont=dict(color='black')))
    
    fig_inflacao = go.Figure(layout=layout)

    fig_inflacao.add_trace(go.Bar(x=dados_inflacao.index, y=dados_inflacao.values,
                                  marker_color='blue', name=valor_do_dropdown_indicador))
    return fig_inflacao


if __name__ == '__main__':
    app.run(debug=True, port=8050)
