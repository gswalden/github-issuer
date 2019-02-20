import os

import yaml
from github import Github

g = Github(os.getenv('GITHUB_TOKEN'))
with open('template.yml') as f:
    my_input = yaml.load(f)

default = my_input['default']

for repo_key, issues in my_input['repos'].items():
    repo = g.get_repo(repo_key)
    for issue in issues:
        if issue['title']:
            fields = {**default, **issue}
            repo.create_issue(**fields)
