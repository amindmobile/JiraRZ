# class Cat:
#     def __init__(self, name):
#         self.name = name
#     def talk(self):
#         return self.name + " says 'meow!'"


# barsik = Cat('Барсик')
# print(barsik.talk())


import numpy as np
import pandas as pd
from settings import all_issues, jira_atl, project, jira2
from ast import literal_eval


# df = pd.read_csv('tasks1.csv', names=['Key', 'Status', 'Type', 'Link'])
# df = pd.read_csv('tasks1.csv', names=['Key', 'Status', 'Type', 'Summary', 'Link'])
df = pd.read_csv('tasks1.csv')
print(df['Link'])
df['Link'] = df['Link'].apply(literal_eval)


def check_link(link):
    return not bool(int(link[-1]) % 2)


def notify(code):
    print(f'{code} is done')


