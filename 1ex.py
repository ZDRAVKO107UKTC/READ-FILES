with open("output.txt", "w") as file:
    file.write("Примерен текст за запис във файл.\n")

with open("output.txt", "r") as file:
    content = file.read()
    print(content)
