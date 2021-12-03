horizontal = 0
depth = 0


for line in open("input.txt", "r"):
    split_line = line.strip().split(" ")
    if split_line[0].lower() == "down":
        depth += int(split_line[1])
    if split_line[0].lower() == "up":
        depth -= int(split_line[1])
    if split_line[0].lower() == "forward":
        horizontal += int(split_line[1])


print(f"Depth: {depth}\nHorizontal: {horizontal}\nProduct: {depth * horizontal}")