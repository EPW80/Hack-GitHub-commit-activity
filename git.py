#!/usr/bin/env python3
from datetime import datetime, timedelta
from pathlib import Path
import random
import subprocess


def git_command(args):
    try:
        subprocess.run(args, check=True)
    except subprocess.CalledProcessError as error:
        print(f"Command '{' '.join(args)}' failed with error:\n{error.output}")


start_date = datetime.now()

commit_messages = (
    f"{(start_date - timedelta(days=i)).strftime('%Y-%m-%d')} rand value: {random.randrange(1, 12)}"
    for i in range(500)
)

Path("test.txt").write_text("\n".join(commit_messages))

git_command(["git", "add", "test.txt"])

for message in commit_messages:
    git_command(["git", "commit", "--date", message.split()[0], "-m", "1"])
