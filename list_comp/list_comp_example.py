import pandas as pd


df = pd.read_csv('/Users/ea/Programming/Python/pyprojects/pyprojs_4_learning/list_comp/survey_results_public.csv')
try:
    value = df['YearsCode']
except KeyError:
    print("Key 'YearsCode' not found.")


# years_code_list = list(DataFrame['YearsCode'].dropna())
# print(years_code_list)
