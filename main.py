from functions import Rz
import pandas as pd
from ast import literal_eval
from settings import jira2, all_issues
from time import perf_counter
import multiprocessing as mp
import timeit


# rz = Rz()
# processes = []
# start = perf_counter()

# Вспомогательная функция-шаблон для отправки уведомлений о полностью завершенной User Story
def notify(task_id):
    print(f'{task_id} is done.')


# Read CSV to dada frame. Trying to parse list in list in df 'Link' column
def issues_csv_filter():
    df = pd.read_csv('tasks.csv')
    df = df[(df['Status'] == 'ToDo') & (df['Type'] == 'User Story') & (df['Link'] != '[]') & df.Link.apply(literal_eval)]
    pd.concat([df, pd.DataFrame(df.Link.tolist())], 1)
    print(df)

    issues_csv_filter()

    # for id_ in df['Link']:
    #     for j in list(id_):
    #         print(j)

    # for string_ in df.Link.apply(literal_eval):
    #     for task_id in string_:
    #         print(task_id)

# Распечатать строки+столбцы на выбор
# for index, row in df.iterrows():
#     print(row['Status'], row['Link'])


# df.to_csv('tasks1.csv', index=False)


# for _ in range(8):
#     p = mp.Process(target=issues_csv_filter)
#     p.start()
#     processes.append(p)
#
# for process in processes:
#     process.join()

# finish = perf_counter()
# print(f'Finished in {round(finish - start, 2)} second(s)')


# rz.issues_csv_filter()


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
