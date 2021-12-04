numbers: list[int] = [int(i) for i in open("input.txt")]

total = 0


for i in range(1, len(numbers)):
    if numbers[i] > numbers[i-1]:
        total += 1


print(f"Total: {total}")