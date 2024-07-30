# HEXACO Personality Visualization Project

## Description:

This project is based on data from the HEXACO psychological assessment tool (https://hexaco.org/). The HEXACO acronym comes from these six dimensions of personality measured: Honesty-Humility, Emotionality, eXtraversion, Agreeableness (versus Anger), Conscientiousness, and Openness to Experience.

The survey itself consists of 100 questions, each mapped to one of the six personality dimensions. Respondents rate each question on a 5-point Likert scale, from 1 (strongly disagree) to 5 (strongly agree).

This project simulates 200 respondents, calculates their scores, and then displays the output using Plotly visualizations in a web UI using Dash.

Inspiration for this project taken from https://github.com/salastro/hexaco-person/blob/main/README.md

## How to Install & Run

This project uses a number of Python packages and tools. Start by running `main.py`; this is the single-source-of-truth file.

![Image of where to click in VSCode to run a file](https://github.com/erincodes/hexaco-personality-viz/blob/main/images/run-file-VS-Code.png)

Your terminal will likely prompt you with a few packages to `pip` install, including but not limited to:

- Pandas: https://pandas.pydata.org/getting_started.html
- Plotly: https://plotly.com/python/getting-started/
- Dash: https://dash.plotly.com/installation

Refer to the documentation linked above for additional installation troubleshooting as needed.

Once all packages are installed, `main.py` will fully run and a message like this will appear in your terminal: `Dash is running on http://127.0.0.1:8050/`. Navigate to the link provided to view the interactive web UI.

![Example of expected output in web browser](https://github.com/erincodes/hexaco-personality-viz/blob/main/images/output-iu-example.png)

## Potential Gotchas:

Presently, if you want to see different results in the web output, you will need to re-run `main.py`. A potential future enhancement is to include a way to regenerate a new group of X users from the UI and see what changes.

## File Structure:

- data = Generated data files used during development and testing. Keeping these to demonstration the project's evolution, but ultimately am managing data purely through Pandas dataframes.
- docs = Resource and reference documentation files
- examples_prof = Example files and ideas from Professor Harding
- images = Screenshots to enhance project documentation
- `main_debug.py` = Debugging version of Jupyter notebook, used during development & testing to troubleshoot
- `main.ipynb` = Jupyter notebook of main functionality, used during development & testing
- `main.py` = Source-of-truth runnable file
