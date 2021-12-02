aim = 0
horizontal = 0
depth = 0

for line in open("input.txt", "r"):
    split_line = line.strip().split(" ")
    if split_line[0].lower() == "forward":
        horizontal += int(split_line[1])
        if aim != 0:
            depth += aim * int(split_line[1])
    if split_line[0].lower() == "up":
        aim -= int(split_line[1])
    if split_line[0].lower() == "down":
        aim += int(split_line[1])

print(f"Horizontal: {horizontal}\n"
      f"Depth: {depth}\n"
      f"Aim: {aim}\n"
      f"Product: {depth * horizontal}"
)
