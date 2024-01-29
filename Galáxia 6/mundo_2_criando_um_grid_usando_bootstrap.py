from dash import Dash, html, dcc, callback, Output, Input, dash_table
import dash_bootstrap_components as dbc

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = dbc.Container(
    [

    dbc.Row(
    
        [
            
            dbc.Col('Teste 1', style={'background-color':'green', 'margin':'8px'}),
            
            dbc.Col('Teste 2', style={'background-color':'blue', 'margin':'8px'})
        
        ], 
        
        style={'height':'50vh'}
    
    ),

    dbc.Row(
    
        [
            
            dbc.Col('Teste 3', style={'background-color':'yellow', 'margin':'8px'}),
            
            dbc.Col('Teste 4', style={'background-color':'red', 'margin':'8px'})
    
        ], 
        
        style={'height':'50vh'}
    
    )
    
    ], 
    
    style={'max-width':'100%'}
    
)


if __name__ == '__main__':
    app.run(debug=True, port=8050)
