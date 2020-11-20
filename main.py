from functions import Rz
import pandas as pd
from ast import literal_eval
from settings import jira2, all_issues
from time import perf_counter

# rz = Rz()

start = perf_counter()


def issues_csv_filter():
    df = pd.read_csv('tasks.csv')
    df = df[(df['Status'] == 'ToDo') & (df['Type'] == 'User Story') & (df['Link'] != '[]')]
    df['Link'] = df.Link.apply(literal_eval)
    df.to_csv('tasks1.csv', index=False)


issues_csv_filter()
finish = perf_counter()
print(f'Finished in {round(finish - start, 2)} second(s)')


#rz.issues_csv_filter()


# df = pd.read_csv('tasks1.csv')
# df['Link'] = df.Link.apply(literal_eval)
# print(df.head())

# Попытка вытащить ID из вложенного списка.
# for id in literal_eval(df['Link']):
#     for i in id:
#         print(i)


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
