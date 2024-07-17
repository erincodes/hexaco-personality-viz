
# Import packages
from dash import Dash, html, dash_table, dcc
import pandas as pd
import plotly.express as px

# Incorporate data
df = pd.read_csv('data/combined-scores.csv')

# Initialize the app
app = Dash()

# App layout
app.layout = [
    html.Div(children='My First App with Data and a Graph'),
    dash_table.DataTable(data=df.to_dict('records'), page_size=10),
    # dcc.Graph(figure=px.histogram(df, x='h', y='e', histfunc='avg'))
    dcc.Graph(figure=px.histogram(df, x='h', y='e'))
]

# Run the app
if __name__ == '__main__':
    app.run(debug=True)