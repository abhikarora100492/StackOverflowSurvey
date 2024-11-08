#%%
# import liabraries
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import textwrap
import openpyxl
#%%
# import raw data
qname_levels_single_response_crosswalk = pd.read_csv('https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2024/2024-09-03/qname_levels_single_response_crosswalk.csv')
stackoverflow_survey_questions = pd.read_csv('https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2024/2024-09-03/stackoverflow_survey_questions.csv')
stackoverflow_survey_single_response = pd.read_csv('https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2024/2024-09-03/stackoverflow_survey_single_response.csv')
# %%
# function to analyze raw datasets
def analyze_dataframes(dataframes):
    for i, df in enumerate(dataframes, 1):
        print(f"\n--- DataFrame {i} Analysis ---\n")
        
        print("Info:")
        df.info()
        
        print("\nDescribe:")
        print(df.describe())
        
        print("\nShape:")
        print(df.shape)
        
        print("\nColumn Names:")
        print(df.columns.tolist())
        
        print("\nNull/NaN Count per Column:")
        print(df.isnull().sum())
        
        print("\nPercentage of Null/NaN Values per Column:")
        print((df.isnull().sum() / len(df)) * 100)
        
        print("\nFirst 5 rows:")
        print(df.head())
        
        print("\n" + "="*50 + "\n")

# Assuming your DataFrames are named as follows:
dataframes = [qname_levels_single_response_crosswalk, 
              stackoverflow_survey_questions, 
              stackoverflow_survey_single_response]

# Call the function
analyze_dataframes(dataframes)
# %%
# coverting the wide df to long df
df_responses_long = pd.melt(stackoverflow_survey_single_response, 
                  id_vars=['response_id'], 
                  var_name='qname',
                  value_name='response')
#%%
# Sort by response_id for better readability
df_responses_long = df_responses_long.sort_values('response_id').reset_index(drop=True)
#%%
# creating response variables 
response_stats = df_responses_long.groupby(['qname','response']).agg({'response':[
    ('frequencies', lambda x: x.value_counts())]}).reset_index()

response_stats.columns = ['_'.join(col).strip() for col in response_stats.columns.values]

response_stats.columns = ['qname', 'response', 'response_frequencies']
#%%
# creating Qs variable 

qname_stats = df_responses_long.groupby('qname').agg({
    'response_id': [('possible_responses','max')],
    'response': [
        ('no_response', lambda x: x.isnull().sum()),
        ('total_responses', 'count'),
        ('response_options', lambda x: x.nunique())
    ]
}).reset_index(False)

qname_stats.columns = ['_'.join(col).strip() for col in qname_stats.columns.values]
qname_stats.columns = ['qname', 'possible_responses', 'no_responses', 'total_responses', 'response_options']

# Adding question type variable 

question_type = pd.merge(pd.DataFrame({'qname':df_responses_long['qname'].unique()}).reset_index(drop = True)
,pd.DataFrame({'qname': qname_levels_single_response_crosswalk['qname'].unique()}).reset_index(drop = True)
, how='left',on='qname', indicator=True)
question_type.columns = ['qname', 'merge'] 
question_type['type'] = question_type['merge'].case_when([
    (question_type['merge'] == 'both', 'with_options'),
    (question_type['merge'] == 'left_only', 'without_options')
]) 
qname_stats = pd.merge(qname_stats, question_type[['qname','type']], how='left', on='qname')
#%%
# merging the question variables & response variables in one df
qname_response_stats = pd.merge(response_stats, qname_stats, how='left', on='qname')
qname_response_stats['no_response_percent'] = round(qname_response_stats['no_responses']/qname_response_stats['possible_responses']*100,2)
qname_response_stats['response_frequency_percent'] = round(qname_response_stats['response_frequencies']/qname_response_stats['total_responses']*100,2)
# merging and adding response text
qname_response_stats = pd.merge(qname_response_stats, qname_levels_single_response_crosswalk, how='left', left_on=['qname','response'], right_on=['qname', 'level'])
#merging and adding qname text 
qname_response_stats = pd.merge(qname_response_stats, stackoverflow_survey_questions, how='left', on='qname')
# %%
# export to excel 
qname_response_stats.to_excel('qname_response_stats.xlsx')

# %%
