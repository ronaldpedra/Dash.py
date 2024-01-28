from dash import Dash, html, dcc, callback, Output, Input, dash_table
import yfinance as yf
import datetime

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

app = Dash(__name__)

app.layout = html.Main(

    children = [
        html.Div(children=[
            html.Div(
                html.H1(children='Cotações de Ontem', style={'color':'white', 'border':'1px solid #08F7FE', 'border-radius':'8px', 'padding':'8px'}), 
                style={'display':'flex', 'justify-content':'center'}),

            html.Div(children=dash_table.DataTable(cotacoes.to_dict('records'), id='tabela_teste'))
            ], 
            style={'background-color':'black', 'grid-columns':'1', 'grid-row':'1', 'height':'50vh'}),

        html.Div(children='Texto 2', style={'background-color':'black', 'grid-columns':'1', 'grid-row':'2', 'height':'50vh'}),
        html.Div(children='Texto 3', style={'background-color':'black', 'grid-columns':'2', 'grid-row':'1', 'height':'50vh'}),
        html.Div(children='Texto 4', style={'background-color':'black', 'grid-columns':'2', 'grid-row':'2', 'height':'50vh'})
    ],
    style={'display':'grid', 'gap':'25px', 'grid-template-columns':'repeat(2, 1fr)'}
)

if __name__ == '__main__':
    app.run(debug=True)
