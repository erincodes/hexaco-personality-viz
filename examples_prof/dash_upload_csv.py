import base64
import io
import pandas as pd
from dash import Dash, html, dcc
from dash.dependencies import Input, Output, State
import datetime

app = Dash(__name__)

app.layout = html.Div([
	dcc.Upload(
		id='upload-data',
		children=html.Div([
			'Drag and Drop or ',
			html.A('Select Files')
		]),
		style={
			'width': '100%',
			'height': '60px',
			'lineHeight': '60px',
			'borderWidth': '1px',
			'borderStyle': 'dashed',
			'borderRadius': '5px',
			'textAlign': 'center',
			'margin': '10px'
		},
		# Allow multiple files to be uploaded
		multiple=True,
		# Accept only CSV files
		accept='.csv'
	),
	html.Div(id='output-data-upload'),
])

def parse_contents(contents, filename, date):
	content_type, content_string = contents.split(',')
	decoded = base64.b64decode(content_string)
	try:
		if 'csv' in filename:
			# Assume that the user uploaded a CSV file
			df = pd.read_csv(io.StringIO(decoded.decode('utf-8')))

            # you only need to return something if you want to display the data
            # which for 2000 rows might be a bit much :)
			return html.Div([
				html.H5(filename),
				html.H6(datetime.datetime.fromtimestamp(date)),
				html.Pre(df.head().to_string())
			])
	except Exception as e:
		print(e)
		return html.Div([
			'There was an error processing this file.'
		])

@app.callback(Output('output-data-upload', 'children'),
			  Input('upload-data', 'contents'),
			  State('upload-data', 'filename'),
			  State('upload-data', 'last_modified'))
def update_output(list_of_contents, list_of_names, list_of_dates):
	if list_of_contents is not None:
		children = [
			parse_contents(c, n, d) for c, n, d in zip(list_of_contents, list_of_names, list_of_dates)
		]
		return children

if __name__ == '__main__':
	app.run_server(debug=True)