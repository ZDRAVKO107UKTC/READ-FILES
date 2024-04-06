with open("numbers.txt", "w") as file:
    for i in range(1, 11):
        file.write(str(i) + "\n")
