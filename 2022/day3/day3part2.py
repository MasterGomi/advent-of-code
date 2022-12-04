LOWER_START = ord('a')
LOWER_OFFSET = 1 - LOWER_START
LOWER_END = LOWER_START + 26
UPPER_START = ord('A')
UPPER_OFFSET = 27 - UPPER_START
UPPER_END = UPPER_START + 26

f = open(r"C:\Code\advent\2022\day3\day3input.txt")

total_priority = 0
elf_groups = [[]]

i = 0
elves = 0
for line in f:
    elf_groups[i].append(line)
    elves += 1
    if elves is 3:
        elves = 0
        i += 1
        elf_groups.append([])

for elf_group in elf_groups:
    # The last'll be empty, skip it
    if not elf_group:
        continue
    # Unpack
    elf1, elf2, elf3 = elf_group

    # Probably not the nicest, but it'll work
    dupe_char_code = 0
    for c in elf1:
        if c in elf2 and c in elf3:
            dupe_char_code = ord(c)
            break
    if LOWER_START <= dupe_char_code <= LOWER_END:
        total_priority += dupe_char_code + LOWER_OFFSET
    else:
        total_priority += dupe_char_code + UPPER_OFFSET

print("Done. Total priority of duped items is: " + str(total_priority))