from collections import namedtuple

with open("../inputs/09", "r") as f:
    disk_map = f.read()


File = namedtuple("File", ["position", "length"])

disk_map = list(map(int, disk_map))
# file_lengths, free_space = disk_map[::2], disk_map[1::2]

memory = []
idx = 0
files: dict[int, File] = {}
free: list[File] = []
for i, val in enumerate(disk_map):
    if i % 2 == 0:
        files[idx] = File(len(memory), val)
        memory.extend([idx] * val)
        idx += 1
    else:
        free.append(File(len(memory), val))
        memory.extend(["."] * val)

keep_index = idx

left = 0
right = len(memory) - 1
while left < right:
    if memory[left] == ".":
        while memory[right] == ".":
            right -= 1

        memory[left], memory[right] = memory[right], memory[left]
        right -= 1
    left += 1


idx = 0
total = 0
while memory[idx] != ".":
    total += idx * memory[idx]
    idx += 1

print(total)

idx = keep_index

# Part 2
while idx > 0:
    idx -= 1
    file = files[idx]

    for i, block in enumerate(free):
        if block.position >= file.position:
            free = free[:i]
            break

        if block.length == files[idx].length:
            free.pop(i)
            files[idx] = File(block.position, file.length)
            break
        if block.length > file.length:
            files[idx] = File(block.position, file.length)
            free[i] = File(block.position + file.length, block.length - file.length)
            break


total = 0
for idx, file in files.items():
    for i in range(file.length):
        total += idx * (file.position + i)

print(total)
