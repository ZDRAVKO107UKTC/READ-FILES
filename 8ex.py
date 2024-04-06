with open("file1.txt", "r") as file1, open("file2.txt", "r") as file2, open("merged.txt", "w") as merged_file:
    merged_file.write(file1.read())
    merged_file.write(file2.read())
