import os
from datetime import datetime

filename = "temp.txt"

if os.path.exists(filename):
    os.remove(filename)

with open(filename, "w") as file:
    file.write(f"Текуща дата и час: {datetime.now()}\n")
