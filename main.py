from functions import Rz
import pandas as pd
from settings import jira2, all_issues

# Construct issues to CSV
rz = Rz()


def asas():
    df = pd.read_csv('tasks.csv')
    df = df[(df['Status'] == 'ToDo') & (df['Type'] == 'User Story') & (df['Link'] != '[]')]
    df.to_csv('tasks1.csv', index=False)
    # print(type(df.loc[6, 'Link']))
    # print(df.loc['Link', 8])
    # # df1 = df[(df['Status'] == 'ToDo') & (df['Type'] == 'User Story') & (df['Link'].astype(bool) != '[]')]


#     print(df[df["Link"] == "[]"])
#    return df[df("Status") == "ToDo" and df("Type") == "User Story"]
#    return type(df.loc[8, df['Link']])
#    return df.loc[8, ['Link']]


# rz.issues_construct()
# asas()
rz.issues_csv_parse()

# print(all_issues)
# print(jira2.fields())
# "JiraIssueLink" in df['Link']

# construct_issues()

# return df[(df['Status'] == 'ToDo') & df[c].isin([d, e, f])]
# df1.loc['a', 'A']

