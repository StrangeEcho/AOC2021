numbers: list[int] = [int(i) for i in open("input.txt")]

sum_list: list[int] = []

total = 0


for index in range(2, len(numbers)):
    sum_list.append(numbers[index] + numbers[index-1] + numbers[index-2])

    
for index in range(1, len(sum_list)):
    if sum_list[index] > sum_list[index-1]:
        total += 1


print(f"Total: {total}")