char_to_find = "A"

with open("input.txt", "r") as input_file, open("output.txt", "w") as output_file:
    for line in input_file:
        if line.startswith(char_to_find):
            output_file.write(line)
