import os
import re
import sys
from github import Github

def write_issue_to_file(issues):
    for issue in issues:
        file = '_posts/'+ issue.created_at.strftime("%Y-%m-%d") + '-' + str(issue.number) + '.md'
        with open(file, "a") as f:
            f.write('---\n')
            if issue.body is not None:
                f.write (issue.body + '\n')
            f.write('---\n')
        f.close()
        issue.edit(state='closed')
        print('Finished with ' + issue.title)

if __name__ == '__main__':
    repoUrl = 'bgzo/One'

    token = sys.argv[1]
    g = Github(token)
    repo = g.get_repo(repoUrl)
    name = g.get_user().login
    issues = repo.get_issues(   labels=['Quote'],
                                state='open',
                                creator=name,
                                sort='updated')

    write_issue_to_file(issues)
