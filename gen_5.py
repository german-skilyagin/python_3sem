def generate_head(file_path, num_lines):
    with open(file_path, 'r') as file:
        for i, line in enumerate(file):
            if i >= num_lines:
                break
            yield line.rstrip('\n')

for line in generate_head('example.txt', 3):
    print(line)