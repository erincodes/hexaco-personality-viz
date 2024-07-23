import dash
from dash import html, dcc, callback, Input, Output, State
from main import questions_dict
import pandas as pd


# Just need a list of questions
questions100 = [v for v in questions_dict.values()]

# Initialize the Dash app
app = dash.Dash(__name__)

# Define the layout of the app
app.layout = html.Div([
    dcc.Store(id='ratings-store', data=[]),  # To store the ratings
    dcc.Store(id='current-index', data=0),  # To keep track of the current question index
    html.Div(id='question-text', style={'fontSize': '18px'}),
    dcc.Slider(
        id='rating-slider',
        min=1,
        max=5,
        step=1,
        value=3,
        marks={
        1: {'label': 'Strongly Disagree ', 'style': {'textAlign': 'center', 'fontSize': '18px'}},
        2: {'label': 'Disagree', 'style': {'textAlign': 'center', 'fontSize': '18px'}},
        3: {'label': 'Neutral', 'style': {'textAlign': 'center', 'fontSize': '18px'}},
        4: {'label': 'Agree', 'style': {'textAlign': 'center', 'fontSize': '18px'}},
        5: {'label': 'Strongly Agree', 'style': {'textAlign': 'center', 'fontSize': '18px'}},
    }
    ),
    html.Div([
        html.Button('Submit', id='submit-button', n_clicks=0)
    ], style={'textAlign': 'center', 'fontSize': '20px', 'marginTop': '20px'}),
    html.Div(id='output-container', style={'fontSize': '16px'})
], style={'width': '500px', 'fontSize': '16px', 'margin': 'auto'})

# Callback to update the question text
@callback(
    Output('question-text', 'children'),
    Output('rating-slider', 'value'),
    Input('submit-button', 'n_clicks'),
    State('current-index', 'data'),
    State('ratings-store', 'data'),
    State('rating-slider', 'value')
)
def update_question(n_clicks, current_index, ratings, rating_value):
    if n_clicks > 0:
        # Save the current rating
        ratings.append(rating_value)
        # Move to the next question
        current_index += 1
        if current_index < len(questions100):
            # Update the question text and reset the slider
            return f"Question {current_index} of 100: {questions100[current_index]}", 3
        else:
            # If all questions have been answered, disable the submit button and show a message
            return "All questions have been rated. Thank you!", 3
    # Initial load
    return questions100[current_index], 3

# Callback to save the ratings and current index
@callback(
    Output('ratings-store', 'data'),
    Output('current-index', 'data'),
    Input('submit-button', 'n_clicks'),
    State('current-index', 'data'),
    State('ratings-store', 'data'),
    State('rating-slider', 'value'),
    prevent_initial_call=True
)
def save_rating(n_clicks, current_index, ratings, rating_value):
    ratings.append(rating_value)

    # save to csv file using pandas
    df = pd.DataFrame(ratings)
    df.to_csv('ratings.csv', index=False)

    return ratings, current_index + 1

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)