import os

filename = "test.txt"

if os.path.exists(filename):
    open(filename, 'w').close()
    print(f"Файлът '{filename}' е изтрит и съдържанието му е празно.")
else:

    with open(filename, "w") as file:
        file.write("Примерно съдържание.\n")
    print(f"Създаден е нов файл '{filename}' със съдържание.")
