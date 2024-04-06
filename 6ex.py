import os
from datetime import datetime

filename = "log.txt"

if os.path.exists(filename):
    with open(filename, "a") as file:
        file.write(f"Изпълнение на програмата на {datetime.now()}\n")
else:
    with open(filename, "w") as file:
        file.write("Стартиране на програмата.\n")
