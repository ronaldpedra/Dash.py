from dash import Dash, html, dcc, callback, Output, Input, dash_table
import yfinance as yf
import datetime
import plotly.graph_objects as go

ticker = ['WEGE3', 'PETR4', 'ABEV3', 'VALE3', 'MGLU3', 'PCAR3', 'ITUB4', 'BBDC4', 'BBAS3']
ticker_yahoo = [ticker + '.SA' for ticker in ticker]

cotacoes = yf.download(ticker_yahoo, start=(datetime.date.today() - datetime.timedelta(days=5)))
cotacoes = cotacoes['Close']
cotacoes = cotacoes.iloc[-1, :]
cotacoes = cotacoes.to_frame()
cotacoes = cotacoes.reset_index()
cotacoes.columns = ['Ticker', 'Preço']
cotacoes['Ticker'] = ticker
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

app = Dash(__name__)

app.layout = html.Main(

    children = [
        html.Div(children=[
            html.Div(
                html.H1(children='Cotações de Ontem', style={'color':'white', 'border':'1px solid #08F7FE', 'border-radius':'8px', 'padding':'8px'}), 
                style={'display':'flex', 'justify-content':'center'}),

            html.Div(children=dash_table.DataTable(cotacoes.to_dict('records'), id='tabela_teste',
                                                   style_header={
                                                       'backgroundColor':'#333E66',
                                                       'fontWeight':'bold',
                                                       'border':'0px',
                                                       'font-size':'12px',
                                                       'color':'#D3D6DF',
                                                       'borderRadius':'8px'
                                                   },
                                                   style_cell={
                                                       'textAlign':'center',
                                                       'padding':'4px 4px',
                                                       'backgroundColor':'#212946',
                                                       'borderRadius':'8px',
                                                       'color':'#D3D6DF'
                                                   },
                                                   style_data={
                                                       'border':'0px',
                                                       'font-size':'12px'
                                                   },
                                                   style_table={
                                                       'borderRadius':'8px',
                                                       'overflow':'hidden'
                                                   },
                                                   style_data_conditional=[
                                                       {
                                                           'if':{
                                                               'filter_query':'{Preço} > 20',
                                                               'column_id':['Preço', 'Ticker'],
                                                            },
                                                               'color':'#19C819'
                                                        },
                                                        {
                                                            'if':{
                                                                'filter_query':'{Preço} < 20',
                                                                'column_id':'Preço'
                                                            },
                                                                'color':'#E50000'
                                                        }
                                                    ]
                                                   ),
                                                   style={'margin-left':'100px', 'margin-right':'100px'}
            )
        ], 
        style={'background-color':'black', 'grid-columns':'1', 'grid-row':'1', 'height':'50vh'}),

        html.Div(children=[
            html.Div(
                html.H1(children='Gráfico de Candle', style={'color':'white', 'border':'1px solid #08F7FE', 'border-radius':'8px', 'padding':'8px'}), 
                style={'display':'flex', 'justify-content':'center'}),

            html.Div(children=dcc.Graph(figure=fig_candle, style={'margin-left':'100px', 'margin-right':'100px', 'height':'400px'})

            )
        ], 
        style={'background-color':'black', 'grid-columns':'1', 'grid-row':'2', 'height':'50vh'}),

        html.Div(children=[
            html.P('Elementos do Dash'),
            dcc.Dropdown(['IPCA', 'IGP-M'], 'IPCA', id='escolher_inflacao', multi=True),
            html.Br(),
            dcc.Checklist(['IPCA', 'IGP-M'], id='checklist-padrao'),
            html.Br(),
            dcc.Slider(0, 30, 5)
        ], 
                 style={'background-color':'white', 'grid-columns':'2', 'grid-row':'1', 'height':'50vh'}),

        html.Div(children='Texto 4', style={'background-color':'black', 'grid-columns':'2', 'grid-row':'2', 'height':'50vh'})
    ],
    style={'display':'grid', 'gap':'25px', 'grid-template-columns':'repeat(2, 1fr)'}
)

if __name__ == '__main__':
    app.run(debug=True)
