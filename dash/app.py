
# Import packages
from dash import Dash, html, dash_table, dcc, callback, Output, Input
import pandas as pd
import plotly.express as px

# Incorporate data
df = pd.read_csv('data/combined-scores.csv')

# Initialize the app
app = Dash()

# App layout
app.layout = [
    html.Div(children='My First App with Data, Graph, and Controls'),
    html.Hr(),
    # dcc.RadioItems(options=['pop', 'lifeExp', 'gdpPercap'], value='lifeExp', id='controls-and-radio-item'),
    # 'Honesty-Humility', 'Emotionality', 'eXtraversion', 'Agreeableness', 'Conscientiousness', 'Openness']
    dcc.RadioItems(options=['h', 'e', 'x', 'a', 'c', 'o'], value='x', id='controls-and-radio-item'),
    dash_table.DataTable(data=df.to_dict('records'), page_size=10),
    # dcc.Graph(figure=px.histogram(df, x='h', y='e', histfunc='avg'))
    dcc.Graph(figure={}, id='controls-and-graph')
]
# Add controls to build the interaction
@callback(
    Output(component_id='controls-and-graph', component_property='figure'),
    Input(component_id='controls-and-radio-item', component_property='value')
)
def update_graph(col_chosen):
    # fig = px.histogram(df, x='h', y=col_chosen, histfunc='avg')
    fig = px.bar(df, x = 'x', y = col_chosen, title='HEXACO Personality Score Comparison')
    return fig

# Run the app
if __name__ == '__main__':
    app.run(debug=True)