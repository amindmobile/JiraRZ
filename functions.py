# Собрать все таски V
# Посчитать все таски V
# Отфильтровать "только: ТуДу"
# Отфильтьровать "только User Story"
# Найти ID каждого линка ведущего к\от Userstory
# ToDo: Найти линки в каждой User Story
# ToDo: Найти статус линков
# ToDo: Отфильтровать по статусу линков "Готово"
# ToDo: Если все линки в User Story в статусе "Готово" - создать уведомление
# ToDo: Создать механизм отправки почтовых уведомлений
# ToDo: Выложить готовое на Гит и Syno
import numpy as np
import pandas as pd
from settings import all_issues, jira_atl, project, jira2
from ast import literal_eval

np.warnings.filterwarnings('ignore', category=np.VisibleDeprecationWarning)


class Rz:
    def __init__(self):
        self.issues_constructed_all = []
        self.issue_numbers = []

    def issues_construct(self):
        for issue in all_issues:
            issue_constructed = (issue.key,
                                 issue.fields.status,
                                 issue.fields.issuetype,
                                 issue.fields.summary,
                                 [issue.id for issue in issue.fields.issuelinks],
                                 )
            self.issues_constructed_all.append(issue_constructed)
        df = pd.DataFrame(np.array(self.issues_constructed_all))
        df.columns = ['Key', 'Status', 'Type', 'Summary', 'Link']
        df.to_csv('tasks.csv', index=False)

# Конструирует ссылки на таски (ссылка + ID)
    def issues_csv_parse(self):
        # df = pd.DataFrame[pd.read_csv('tasks1.csv')].astype(str)
        df = pd.read_csv('tasks1.csv')
        for i in df['Link']:
            # df to list delimiter = ' , '
            # remove 0, -1
            # substring finder
            # replace " ' " -> ''
            # int(list[])

            print('https://www.jira.com/browse/', i)
            # print('\n'.join('jira.com/' + df['Link']))




        # df['Link'].apply(lambda x: x+'http://www.jira.com/browse/')
        # df.to_csv('tasks2.csv')
        # df = pd.to_csv('tasks3.csv')
        # issue = jira_atl.issue('JRA-1330')

    #     # Issues total number count
    # def issues_count(self, list_to_count):
    #     return len(list(list_to_count))
    #
    # def issues_id_collect(self):
    #     for i in jira_atl.get_all_project_issues(project=project, start=0):
    #         self.issue_numbers.append(i)
    #     return self.issue_numbers

    # Get users to data frame
    # def users_get(self):
    #     df_users = pd.DataFrame(data=active_users)
    #     df_users = df_users.T
    #     return df_users

    # Export to excel
    # def write_excel(data_to_write, filename):
    #     data_to_write.to_excel(filename)

# write_excel(get_users(), 'users.xlsx')
# issue_number = '5'
# print(jira.get_issue_status(project + '-' + issue_number))

# Получить список номеров issue
# for i in range по этому списку и дальше цикл ниже

# Find out\inward status
# for link in i.fields.issuelinks:
#     if hasattr(link, "outwardIssue"):
#         outwardIssue = link.outwardIssue
#         print("\tOutward: " + outwardIssue.key)
#     if hasattr(link, "inwardIssue"):
#         inwardIssue = link.inwardIssue
#         print("\tInward: " + inwardIssue.key)
# i.fields.assignee,
# i.fields.summary