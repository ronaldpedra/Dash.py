from dash import Dash, html, dcc, callback, Output, Input

app = Dash(__name__)

app.layout = html.Main(

    children = [
        html.H1('Hello World'),
        html.H2('Subtítulo'),
        html.H3('Sub Subtítulo'),
        html.P('Texto Normal'),
        html.A('Google', href='https://www.google.com'),
        html.A('Globo.com', href='https://www.globo.com', target='_blank', style={'display':'block'}),
    ]
)


if __name__ == '__main__':
    app.run(debug=True)