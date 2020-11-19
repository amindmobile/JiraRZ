from functions import Rz
import pandas as pd
from ast import literal_eval
from settings import jira2, all_issues

rz = Rz()


def asas():
    df = pd.read_csv('tasks.csv')
    df = df[(df['Status'] == 'ToDo') & (df['Type'] == 'User Story') & (df['Link'] != '[]')]
    df['Link'].apply(literal_eval)
    # df.to_csv('tasks1.csv', index=False)


asas()

# Попытка вытащить ID из вложенного списка.
# for id in literal_eval(df['Link']):
#     for i in id:
#         print(i)


    # print(type(df.loc[6, 'Link']))
    # print(df.loc['Link', 8])
    # # df1 = df[(df['Status'] == 'ToDo') & (df['Type'] == 'User Story') & (df['Link'].astype(bool) != '[]')]

    # поработать с этим!
    # df['tasks1.csv'] = df[строка].apply(literal_eval)
#     print(df[df["Link"] == "[]"])
#    return df[df("Status") == "ToDo" and df("Type") == "User Story"]
#    return type(df.loc[8, df['Link']])
#    return df.loc[8, ['Link']]
# ____________________________________________________
# df = pd.read_csv('tasks1.csv', usecols=['Key', 'Link'])
# for i in df['Link']:
#     # df.values.tolist()
#     print(i)
# products_list = df.values.tolist()
# print(products_list)
# ____________________________________________________

# "JiraIssueLink" in df['Link']
