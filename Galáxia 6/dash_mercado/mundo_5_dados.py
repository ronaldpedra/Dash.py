import yfinance as yf
import datetime
import plotly.graph_objects as go
from bcb import sgs


def dados_cotacoes():
    
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

    return cotacoes, ticker_yahoo

def grafico_candle(ticker_yahoo):

    cotacoes_candle = yf.download(ticker_yahoo[0], start=(datetime.date.today() - datetime.timedelta(days=5)))
    cotacoes_candle = cotacoes_candle.dropna()
    
    layout = go.Layout(yaxis=dict(showline=False),
                       xaxis=dict(showline=False),
                       template='darkly')

    fig_candle = go.Figure(data=[go.Candlestick(x=cotacoes_candle.index,
                                                open=cotacoes_candle['Open'],
                                                high=cotacoes_candle['High'],
                                                low=cotacoes_candle['Low'],
                                                close=cotacoes_candle['Close']),
                                                ], layout=layout)
    
    fig_candle.update_xaxes(rangeslider_visible=False,
                            rangebreaks=[
                                dict(bounds=['sat', 'mon']),
                                dict(values=['2015-12-25', '2016-01-01']) # Feriados
                            ])
    
    fig_candle.update_layout(margin=dict(l=16, r=16, t=16, b=16))
    
    return fig_candle

def grafico_inflacao(valor_do_dropdown_indicador, valor_do_dropdown_periodo):
    
    dados_inflacao = sgs.get({'ipca':433, 'igp-m':189})
    dados_inflacao = dados_inflacao.dropna()
    dados_inflacao = dados_inflacao / 100
    dados_inflacao = dados_inflacao.iloc[-(int(valor_do_dropdown_periodo)):, :]

    if valor_do_dropdown_indicador == 'IPCA':
        dados_inflacao = dados_inflacao['ipca']
        
    elif valor_do_dropdown_indicador == 'IGP-M':
        dados_inflacao = dados_inflacao['igp-m']
    
    layout = go.Layout(yaxis=dict(tickformat='.1%'), template='darkly')
    
    fig_inflacao = go.Figure(layout=layout)

    fig_inflacao.add_trace(go.Bar(x=dados_inflacao.index, y=dados_inflacao.values, name=valor_do_dropdown_indicador))

    fig_inflacao.update_layout(margin=dict(l=16, r=16, t=16, b=16))

    return fig_inflacao
