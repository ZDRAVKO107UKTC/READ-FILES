with open("data.txt", "r") as file:
    content = file.read()
    word_count = len(content.split())
    print(f"Брой думи във файла: {word_count}")
