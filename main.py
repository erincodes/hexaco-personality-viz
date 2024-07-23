# Overview of main.py:
# This file is the main executable for the project
# Simulates the HEXACO personality test for X number of participants
# Calculates the scores for each participant across the HEXACO categories
# Stores these scores in a Pandas dataframe (via 1 list of dictionaries participant)
# Serves up Dash app in browser to display data in interactive UI using Plotly data visualizations

################## Imports ##################
# TODO: ESA - remove any imports I don't end up using

import pandas as pd
import random
import plotly.express as px #Equivalent to: import plotly.graph_objects as go
import plotly.graph_objects as go 
from dash import Dash, html, dash_table, dcc, callback, Output, Input

################## Variable Definitions ##################

# Baseline HEXACO test questions:
questions_dict = {
    1   : "I would be quite bored by a visit to an art gallery.",
    2   : "I clean my office or home quite frequently.",
    3   : "I rarely hold a grudge, even against people who have badly wronged me.",
    4   : "I feel reasonably satisfied with myself overall.",
    5   : "I would feel afraid if I had to travel in bad weather conditions.",
    6   : "If I want something from a person I dislike, I will act very nicely toward that person in order to get it.",
    7   : "I'm interested in learning about the history and politics of other countries.",
    8   : "When working, I often set ambitious goals for myself.",
    9   : "People sometimes tell me that I am too critical of others.",
    10  : "I rarely express my opinions in group meetings.",
    11  : "I sometimes can't help worrying about little things.",
    12  : "If I knew that I could never get caught, I would be willing to steal a million dollars.",
    13  : "I would like a job that requires following a routine rather than being creative.",
    14  : "I often check my work over repeatedly to find any mistakes.",
    15  : "People sometimes tell me that I'm too stubborn.",
    16  : "I avoid making \"small talk\" with people.",
    17  : "When I suffer from a painful experience, I need someone to make me feel comfortable.",
    18  : "Having a lot of money is not especially important to me.",
    19  : "I think that paying attention to radical ideas is a waste of time.",
    20  : "I make decisions based on the feeling of the moment rather than on careful thought.",
    21  : "People think of me as someone who has a quick temper.",
    22  : "I am energetic nearly all the time.",
    23  : "I feel like crying when I see other people crying.",
    24  : "I am an ordinary person who is no better than others.",
    25  : "I wouldn't spend my time reading a book of poetry.",
    26  : "I plan ahead and organize things, to avoid scrambling at the last minute.",
    27  : "My attitude toward people who have treated me badly is \"forgive and forget\".",
    28  : "I think that most people like some aspects of my personality.",
    29  : "I don’t mind doing jobs that involve dangerous work.",
    30  : "I wouldn't use flattery to get a raise or promotion at work, even if I thought it would succeed.",
    31  : "I enjoy looking at maps of different places.",
    32  : "I often push myself very hard when trying to achieve a goal.",
    33  : "I generally accept people’s faults without complaining about them.",
    34  : "In social situations, I'm usually the one who makes the first move.",
    35  : "I worry a lot less than most people do.",
    36  : "I would be tempted to buy stolen property if I were financially tight.",
    37  : "I would enjoy creating a work of art, such as a novel, a song, or a painting.",
    38  : "When working on something, I don't pay much attention to small details.",
    39  : "I am usually quite flexible in my opinions when people disagree with me.",
    40  : "I enjoy having lots of people around to talk with.",
    41  : "I can handle difficult situations without needing emotional support from anyone else.",
    42  : "I would like to live in a very expensive, high-class neighborhood.",
    43  : "I like people who have unconventional views.",
    44  : "I make a lot of mistakes because I don't think before I act.",
    45  : "I rarely feel anger, even when people treat me quite badly.",
    46  : "On most days, I feel cheerful and optimistic.",
    47  : "When someone I know well is unhappy, I can almost feel that person's pain myself.",
    48  : "I wouldn’t want people to treat me as though I were superior to them.",
    49  : "If I had the opportunity, I would like to attend a classical music concert.",
    50  : "People often joke with me about the messiness of my room or desk.",
    51  : "If someone has cheated me once, I will always feel suspicious of that person.",
    52  : "I feel that I am an unpopular person.",
    53  : "When it comes to physical danger, I am very fearful.",
    54  : "If I want something from someone, I will laugh at that person's worst jokes.",
    55  : "I would be very bored by a book about the history of science and technology.",
    56  : "Often when I set a goal, I end up quitting without having reached it.",
    57  : "I tend to be lenient in judging other people.",
    58  : "When I'm in a group of people, I'm often the one who speaks on behalf of the group.",
    59  : "I rarely, if ever, have trouble sleeping due to stress or anxiety.",
    60  : "I would never accept a bribe, even if it were very large.",
    61  : "People have often told me that I have a good imagination.",
    62  : "I always try to be accurate in my work, even at the expense of time.",
    63  : "When people tell me that I’m wrong, my first reaction is to argue with them.",
    64  : "I prefer jobs that involve active social interaction to those that involve working alone.",
    65  : "Whenever I feel worried about something, I want to share my concern with another person.",
    66  : "I would like to be seen driving around in a very expensive car.",
    67  : "I think of myself as a somewhat eccentric person.",
    68  : "I don’t allow my impulses to govern my behavior.",
    69  : "Most people tend to get angry more quickly than I do.",
    70  : "People often tell me that I should try to cheer up.",
    71  : "I feel strong emotions when someone close to me is going away for a long time.",
    72  : "I think that I am entitled to more respect than the average person is.",
    73  : "Sometimes I like to just watch the wind as it blows through the trees.",
    74  : "When working, I sometimes have difficulties due to being disorganized.",
    75  : "I find it hard to fully forgive someone who has done something mean to me.",
    76  : "I sometimes feel that I am a worthless person.",
    77  : "Even in an emergency I wouldn't feel like panicking.",
    78  : "I wouldn't pretend to like someone just to get that person to do favors for me.",
    79  : "I’ve never really enjoyed looking through an encyclopedia.",
    80  : "I do only the minimum amount of work needed to get by.",
    81  : "Even when people make a lot of mistakes, I rarely say anything negative.",
    82  : "I tend to feel quite self-conscious when speaking in front of a group of people.",
    83  : "I get very anxious when waiting to hear about an important decision.",
    84  : "I’d be tempted to use counterfeit money, if I were sure I could get away with it.",
    85  : "I don't think of myself as the artistic or creative type.",
    86  : "People often call me a perfectionist.",
    87  : "I find it hard to compromise with people when I really think I’m right.",
    88  : "The first thing that I always do in a new place is to make friends.",
    89  : "I rarely discuss my problems with other people.",
    90  : "I would get a lot of pleasure from owning expensive luxury goods.",
    91  : "I find it boring to discuss philosophy.",
    92  : "I prefer to do whatever comes to mind, rather than stick to a plan.",
    93  : "I find it hard to keep my temper when people insult me.",
    94  : "Most people are more upbeat and dynamic than I generally am.",
    95  : "I remain unemotional even in situations where most people get very sentimental.",
    96  : "I want people to know that I am an important person of high status.",
    97  : "I have sympathy for people who are less fortunate than I am.",
    98  : "I try to give generously to those in need.",
    99  : "It wouldn’t bother me to harm someone I didn’t like.",
    100 : "People see me as a hard-hearted person.",
}

# Question numbers that need to be scored with reversed weighting
reversal = [1, 6, 9, 10, 12, 13, 15, 16, 19, 20, 21, 25, 29, 35, 36, 38, 41,
    42, 44, 50, 51, 52, 54, 55, 56, 59, 63, 66, 70, 72, 74, 75, 76, 77, 79, 80,
    82, 84, 85, 87, 89, 90, 91, 92, 93, 94, 95, 96, 99, 100]

# Questions that map to each HEXACO trait
domains_questions = {
    'h': [6, 12, 18, 24, 30, 36, 42, 48, 54, 60, 66, 72, 78, 84, 90, 96],
    'e': [5, 11, 17, 23, 29, 35, 41, 47, 53, 59, 65, 71, 77, 83, 89, 95],
    'x': [4, 10, 16, 22, 28, 34, 40, 46, 52, 58, 64, 70, 76, 82, 88, 94],
    'a': [3, 9, 15, 21, 27, 33, 39, 45, 51, 57, 63, 69, 75, 81, 87, 93],
    'c': [2, 8, 14, 20, 26, 32, 38, 44, 50, 56, 62, 68, 74, 80, 86, 92],
    'o': [1, 7, 13, 19, 25, 31, 37, 43, 49, 55, 61, 67, 73, 79, 85, 91],
}

################## Helper Methods ##################

def generate_random_responses(): 
    '''Function to generate random responses.'''
    responses = [] 
    for i in range(0, len(questions_dict)):
        responses.append(random.randint(1, 5))
    return responses


def calculate_score(responses, domain_questions, reversal):
    '''Function to calculate scores from responses.'''
    scores = {}
    for domain, questions in domain_questions.items():
        score = 0
        for item in questions:
            if item in reversal:
                score += 5 - responses[item]  
            else:
                score += responses[item]
        scores[domain] = score / len(questions)
    return scores

################## Data Creation ##################

def create_data(num_participants):
    '''Simulate the HEXACO survey for multiple participants and store 
    them as a Pandas dataframe.'''
    data = {}
    for i in range(1, num_participants + 1): 
        random_responses = generate_random_responses()
        score = calculate_score(random_responses, domains_questions, reversal)
        data[i] = score

    # Store the data as a dataframe
    df = pd.DataFrame(data)

    return df   

# Generate simulated personality test data
users = 200
df = create_data(users)

# Capture a version of dataframe that is transposed (flipped)
# Participants are rows and HEXACO scores are columns
data_transposed = df.T

# Use built-in dataframe function to generate descriptive statistics
summary_stats = data_transposed.describe()
mean = summary_stats.loc['mean'] 
std = summary_stats.loc['std']

################## Data Visualizations ##################

# Averages bar graph
horizontal_labels = [ 
    "Honesty-Humility (h)",
    "Emotionality (e)",
    "eXtraversion (x)",
    "Agreeableness (a)",
    "Conscientiousness (c)",
    "Openness (o)"
]

participant_1 = df[1]
participant_2 = df[2]
participant_3 = df[3]
participant_4 = df[4]
participant_5 = df[5]

compare_to_average = go.Figure(
    data=[
        go.Bar(
            name="Average",
            x=horizontal_labels,
            y=mean,
            offsetgroup=0,
        ),
        go.Bar(
            name="Participant 1",
            x=horizontal_labels,
            y=participant_1,
            offsetgroup=1,
        ),
        go.Bar(
            name="Participant 2",
            x=horizontal_labels,
            y=participant_2,
            offsetgroup=2,
        ),
        go.Bar(
            name="Participant 3",
            x=horizontal_labels,
            y=participant_3,
            offsetgroup=3,
        ),
        go.Bar(
            name="Participant 4",
            x=horizontal_labels,
            y=participant_4,
            offsetgroup=4,
        ),
        go.Bar(
            name="Participant 5",
            x=horizontal_labels,
            y=participant_5,
            offsetgroup=5,
        ),
    ],
    layout=go.Layout(
        title="First 5 Participant's Scores, as Compared to the Overall Average:",
        yaxis_title="Score"
    )
)

################## Dash UI App Configuration ##################

# Initialize the app
app = Dash()

# App layout
app.layout = [
    html.H1('HEXACO Personality Generated Data & Visualizations'),
    html.Hr(),
    html.P('Simulated scores data ranging from 1-5 for 200 participants across 6 categories.'),
    html.P('Trait categories are: Honesty-Humility (h), Emotionality (e), eXtraversion (x), Agreeableness (a), Conscientiousness (c), and Openness (o):'),
    dash_table.DataTable(data=data_transposed.to_dict('records'), page_size=10),

    # TODO: ESA - hook up radio buttons for 1 viz 
    # Radio buttons section
    # html.P('Select which trait overview you would like to explore in the graph:'),
    # dcc.RadioItems(options=['h', 'e', 'x', 'a', 'c', 'o'], value='h', id='controls-and-radio-item'),

    # Visualization
    # dcc.Graph(figure={}, id='controls-and-graph'),
    # TODO: ESA - seems like I need more data in my df in order to do additional comparisons
    # dcc.Graph(figure=px.histogram(data, x='h', y='e', histfunc='avg'))

    dcc.Graph(figure=compare_to_average),
]

# # Interaction controls
# @callback(
#     Output(component_id='controls-and-graph', component_property='figure'),
#     Input(component_id='controls-and-radio-item', component_property='value')
# )
# def update_graph(col_chosen):
#     fig = px.histogram(data, x='h', y=col_chosen, histfunc='avg', title='Average of Honest-Humility (h) Values')
#     # fig = px.bar(data, x = 'x', y = col_chosen, title='HEXACO Personality Score Comparison')
#     return fig

# This makes it so it will only run if the script is run directly (main)
# if it is imported into another script it will not run
if __name__ == '__main__':
    app.run(debug=True)