# Stack Overflow Survey 2024 Data Analysis

## Overview

This project analyzes the annual Stack Overflow Developer Survey data using Python & [Looker dashboard](https://lookerstudio.google.com/reporting/bbb1a8ca-f692-4dd6-b252-bfcbd31c6074/page/snxBE/edit?s=pCo2geDtt70).. It processes and explores three datasets related to the survey, performs data transformation, and generates statistical insights. The analysis results are visualized in an interactive dashboard.

## Highlights 
- About 80% of questions offered were filled/completed.
- No surprises here but - multiple choice questions have more questions filled vs open ended questions.
- Most of the respondents are develepors with a favorable stance on AI betwene 25-39 years old.
- Total of 25 questions with 65,000 respondents.

## Data Sources

The analysis uses three CSV files from the [TidyTuesday GitHub repository](https://github.com/rfordatascience/tidytuesday/blob/master/data/2024/2024-09-03/readme.md):
1. qname_levels_single_response_crosswalk.csv
2. stackoverflow_survey_questions.csv
3. stackoverflow_survey_single_response.csv

## Dependencies
Python packages:
- pandas
- numpy
- seaborn
- matplotlib
- textwrap
- openpyxl

## Code Structure

### Data Import
The script begins by importing the necessary libraries and loading the three CSV files into pandas DataFrames.

### Data Analysis Function
A function `analyze_dataframes()` is defined to perform initial analysis on each DataFrame, including:
- Basic info
- Descriptive statistics
- Shape
- Column names
- Null value counts and percentages
- First 5 rows preview

### Data Transformation
The code performs several data transformation steps:
1. Converts the wide DataFrame to long format
2. Creates response variables with frequency statistics
3. Generates question (qname) statistics
4. Merges question and response statistics
5. Adds additional calculated fields and merges with crosswalk and question text data

### Data Export
The final DataFrame `qname_response_stats` is exported to an Excel file named 'qname_response_stats.xlsx'.

## How to Use

1. Ensure all required libraries are installed.
2. Run the script in a Python environment.
3. The script will download the data, perform the analysis, and generate an Excel file with the results.

## Output

The main output is an Excel file 'qname_response_stats.xlsx' containing detailed statistics and information about the survey questions and responses.

## Dashboard

The analysis results are visualized in an interactive dashboard created using Looker Studio. The dashboard is accessible at [this link](https://lookerstudio.google.com/reporting/bbb1a8ca-f692-4dd6-b252-bfcbd31c6074/page/snxBE/edit?s=pCo2geDtt70).

### Dashboard Structure

The dashboard is structured into two main pages:

1. **Overview Page**: Provides a high-level summary of the survey results, including:
   - High-level visualizations for:
     - Question Type
     - % with no response
     - Most popuar responses 

2. **Deep Dive Page**: Offers a more detailed and granular view of the data, including:
   - Respondents characteristics 
   - Stance on AI
   - Stack Overflow usage
3. **About Page**: Provides the full survey questions

This two-page structure allows users to get both a quick snapshot of the most important data points and perform more sophisticated analysis as needed.

## Contributing

Contributions to improve the analysis or extend the dashboard are welcome. Please submit a pull request or open an issue to discuss proposed changes.

## Contact

abhikarora10@gmail.com
