# Customer Review DS-ML

This project is a simple end-to-end customer review analysis workflow for hotel reviews, with a focus on Marriott and Radisson Blu properties. It brings together raw review data, sentiment analysis, exploratory notebooks, and an interactive dashboard so the feedback can be understood more clearly.

The main goal is to turn review text into something useful: identify sentiment, highlight common themes, and present the results in a clean dashboard.

## What this project does

The repository includes:

- review datasets for Marriott and Radisson Blu hotels
- preprocessing and analysis notebooks for exploring the data
- sentiment classification artifacts for both hotel brands
- a Streamlit dashboard for viewing positive and negative review insights

## Project structure

- app.py: the Streamlit dashboard application
- data/: raw and processed review datasets used by the project
- Notebooks/: Jupyter notebooks for analysis and exploration
- artifacts/: saved sentiment model files and tokenizers
- images/: images related to the project
- src/: supporting project files and utilities

## Setup

This project is built with Python. A virtual environment is recommended.

1. Clone the repository
2. Create and activate a virtual environment
3. Install the required packages:

```bash
pip install -r requirements.txt
```

If you run the dashboard for the first time, the app may download NLTK stopwords automatically.

## Running the dashboard

To launch the dashboard locally:

```bash
streamlit run app.py
```

The app reads the processed review data from the data folder and displays visual summaries of positive and negative review themes.

## Data and analysis flow

The workflow is fairly straightforward:

1. Review data is loaded from the CSV files in the data folder.
2. The notebooks explore the reviews, clean the text, and prepare the data for analysis.
3. Sentiment labels are applied using the saved model artifacts.
4. The results are displayed in the Streamlit app for easier inspection.

## Notes

This repository is more focused on analysis and presentation than on building a production-grade system. It is useful for understanding customer feedback patterns, especially in hotel review data.

For a detailed write-up of the analysis and findings, you can read the related article on Medium:

https://medium.com/@jubrilifekoya/marriott-vs-69ce85ece087?sharedUserId=jubrilifekoya

If you want to extend it further, the next natural steps would be to add more hotels, improve the sentiment pipeline, or turn the dashboard into a richer reporting tool.
