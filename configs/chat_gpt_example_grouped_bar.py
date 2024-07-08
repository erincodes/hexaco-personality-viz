import numpy as np
import matplotlib.pyplot as plt

# Example score sets
scores_sets = {
    'Set 1': {'Honesty': 3.5, 'Emotionality': 3.2, 'Extraversion': 3.8, 'Agreeableness': 2.9, 'Conscientiousness': 3.6, 'Openness': 3.7},
    'Set 2': {'Honesty': 2.9, 'Emotionality': 3.7, 'Extraversion': 3.1, 'Agreeableness': 2.7, 'Conscientiousness': 3.2, 'Openness': 3.0},
    'Set 3': {'Honesty': 3.1, 'Emotionality': 3.4, 'Extraversion': 3.5, 'Agreeableness': 3.0, 'Conscientiousness': 3.4, 'Openness': 3.4},
    'Set 4': {'Honesty': 3.0, 'Emotionality': 3.1, 'Extraversion': 3.4, 'Agreeableness': 2.8, 'Conscientiousness': 3.5, 'Openness': 3.3},
    'Set 5': {'Honesty': 3.2, 'Emotionality': 3.6, 'Extraversion': 3.7, 'Agreeableness': 2.9, 'Conscientiousness': 3.5, 'Openness': 3.5},
}
mean_scores = {'Honesty': 3.19, 'Emotionality': 3.43, 'Extraversion': 3.50, 'Agreeableness': 2.94, 'Conscientiousness': 3.44, 'Openness': 3.41}

labels = list(mean_scores.keys())
num_sets = len(scores_sets)

# Prepare data for the grouped bar chart
x = np.arange(len(labels))
width = 0.15

fig, ax = plt.subplots(figsize=(12, 6))

for i, (set_name, scores) in enumerate(scores_sets.items()):
    offset = width * (i - num_sets / 2)
    ax.bar(x + offset, list(scores.values()), width, label=set_name)

# Add the mean scores
ax.bar(x + width * (num_sets / 2), list(mean_scores.values()), width, label='Mean', color='black', alpha=0.7)

# Add labels and title
ax.set_xlabel('HEXACO Domains')
ax.set_ylabel('Scores')
ax.set_title('Comparison of HEXACO Scores Across Different Sets')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()

plt.show()
