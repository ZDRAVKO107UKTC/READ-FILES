import re

with open("data.txt", "r") as file:
    content = file.read()
    clean_content = re.sub(r'[^a-zA-Z0-9\s]', '', content)

with open("clean_data.txt", "w") as file:
    file.write(clean_content)
