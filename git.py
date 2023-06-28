import random
import subprocess
from datetime import datetime, timedelta

for i in range(400):
    d = str(i + 1) + " day ago"
    rand = random.randrange(1, 12)
    with open("test.txt", "w") as file:
        file.write(d + " " + str(rand) + "\n")

    subprocess.run(["git", "add", "test.txt"], check=True)

    try:
        subprocess.run(
            ["git", "commit", "--date", f"2023-{rand}-{d}", "-m", "1"], check=True
        )
    except subprocess.CalledProcessError:
        pass

subprocess.run(["git", "push", "-u", "origin", "main"], check=True)
