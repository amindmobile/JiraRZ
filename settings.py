from atlassian import Jira
from jira import JIRA
from loginpass import project, username, password, url

jira_atl = Jira(url=url, username=username, password=password)
jira2 = JIRA(url, basic_auth=(username, password))

all_issues = jira2.search_issues('project=' + project, maxResults=0, fields='key, status, issuetype, summary, issuelinks')
projects2 = jira2.projects()
keys2 = sorted([project.key for project in projects2])




