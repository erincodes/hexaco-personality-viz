# Developers' Guide

## Overview

This project randomly generates personality profiles in Python based on the HEXACO personality dataset. Then, using Pandas to process the data, the statistical averages were visualized using Plotly. Dash, which Plotly's preferred tool, was used to spin up a local dev server.

Review `README.md` for an introduction to the HEXACO personality test and data sources, as well as the steps to install & run the project.

## File Structure:

- data = Generated data files used during development and testing. Keeping these to demonstration the project's evolution, but ultimately, data is being managed purely through Pandas dataframes (not using these CSVs)
- docs = Resource and reference documentation files
- examples_prof = Example files and ideas from Professor Harding (keeping for reference)
- images = Screenshots to enhance project documentation
- `main_debug.py` = Debugging version of Jupyter notebook, used during development & testing to troubleshoot
- `main.ipynb` = Jupyter notebook of main functionality, used during development & testing
- `main.py` = Source-of-truth runnable file
- `requirements.txt` = List of required packages

# Project Specs

- Refer to the spec documentation included in `/docs`
- Aspects of spec not implemented as of now:
  - Interactive controls in the UI
    - Spec outlined using a dropdown for users to select one of the personality traits to view the data for
    - Ultimately, the way I parsed the data was not conducive with this type of interface. Ideas to enhance included below in "Future Work"

# Walkthrough

- `main.py` is the single-source-of-truth, runnable file

  - Refer to inline comments for details on what each method is doing
  - All data visualization and web server logic also lives in `main.py`

- The frontend of this tool is a web browser UI

  - When the user first lands in the UI, they will see a header, some intro information, and a table output of the simulated personality score data.
    ![View when user lands in UI ](https://github.com/erincodes/hexaco-personality-viz/blob/main/images/output-header-table.png)

- The second aspect of the UI is a bar chart visualization

  - This graph displays the first 5 participant scores, as compared to the overall average score
  - Hover over each bar for additional insights
  - User can also hide/show which participant data is displayed by clicking on the participant list on the right-hand side
  - Various built-in Plotly controls to zoom, download as a PNG, etc. are also visible on hover

  ![Bar chart](https://github.com/erincodes/hexaco-personality-viz/blob/main/images/output-averages-bar.png)

- The final aspect of the UI is a scatter plot visualization

  - This displays the average for each trait for first 5 participants scores
  - Hover over each data point for additional insights
  - User can also hide/show which participant data is displayed by clicking on the participant list on the right-hand side
  - Various built-in Plotly controls to zoom, download as a PNG, etc. are also visible on hover

  ![Scatter plot](https://github.com/erincodes/hexaco-personality-viz/blob/main/images/output-standard-deviation-scatter.png)

# Known Issues

- If you encounter any issues when running `main.py` on a Mac, recommend selecting a virtual environment (venv) kernel
- The Dash local dev server will crash anytime you have an error. This can make things challenging when trying to refresh the UI to debug
- If your hot reload isn't working, look to your terminal where you ran `main.py` and check for error messages as your first line of defense
- If you want to see different results in the web output, you will need to re-run `main.py`. Ideas of how to enhance this included below in "Future Work"

# Future Work

- Regenerate a new group of users from the UI
  - Add a number input that represents the number of participants
  - Add a "regenerate" button that a user can click to dynamically repopulate the results from the frontend
- Additional interactive controls
  - Dash has a functionality called "callbacks" that I started to play around with
  - Use callbacks to further build out the user's ability make selections and control what data they are seeing
- Styling enhancements
  - Dash provides styling utilities through Dash Core Components
- Ability for user to actually take the personality test
  - It's 100 questions, which would be time consuming for the user, but it would be cool to serve up individualized results
- Unit testing as functional complexity increases
- There are no known computational inefficiencies at this time, but enhancements to the current methods & logic are welcomed
  - Break methods into modules as complexity increases
