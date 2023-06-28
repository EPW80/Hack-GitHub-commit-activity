#!/usr/bin/env python3
import subprocess
import random
from datetime import datetime, timedelta

commit_messages = []
for i in range(400):
    date = datetime.now() - timedelta(days=i)
    formatted_date = date.strftime("%Y-%m-%d")
    rand = random.randrange(1, 12)
    commit_messages.append(formatted_date)

with open("test.txt", "a") as file:
    file.write("\n".join(commit_messages))
subprocess.run(["git", "add", "test.txt"], check=True)

for message in commit_messages:
    subprocess.run(["git", "commit", "--date", message, "-m", "1"], check=True)

subprocess.run(["git", "push", "-u", "origin", "main"], check=True)

# git commit --amend --no-edit --date="Fri Nov 6 20:00:00 2015 -0600"
# git fetch origin master
# git rebase origin/master
