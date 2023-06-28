#!/usr/bin/env python3
import random
import subprocess
from datetime import datetime, timedelta

with open("test.txt", "a") as file:
    for i in range(400):
        d = str(i) + "days ago"
        rand = random.randrange(1, 12)
        file.write(d + "\n")

subprocess.run(["git", "add", "test.txt"], check=True)

for i in range(400):
    d = str(i) + "days ago"
    rand = random.randrange(1, 12)
    subprocess.run(
        ["git", "commit", "--date", f"2023-{rand}-{d}", "-m", "1"], check=True
    )

subprocess.run(["git", "push", "-u", "origin", "main"], check=True)
