import pandas as pd
import plotly.express as px

df = pd.read_csv('data/0_random_scores.csv')
df.head()
print(df)

fig = px.bar(df, x = 'Domain', y = 'Score', title='HEXACO Personality Score Comparison')
fig.show()