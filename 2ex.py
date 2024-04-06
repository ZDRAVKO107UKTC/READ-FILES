with open("data.txt", "a") as file:
    while True:
        text = input("Въведете текст (за край натиснете 'end'): ")
        if text.lower() == "end":
            break
        file.write(text + "\n")

with open("data.txt", "r") as file:
    content = file.read()
    print(content)
