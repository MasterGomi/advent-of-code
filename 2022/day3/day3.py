LOWER_START = ord('a')
LOWER_OFFSET = 1 - LOWER_START
LOWER_END = LOWER_START + 26
UPPER_START = ord('A')
UPPER_OFFSET = 27 - UPPER_START
UPPER_END = UPPER_START + 26

f = open(r"C:\Code\advent\2022\day3\day3input.txt")

total_priority = 0

for line in f:
    rucksack_size = len(line)
    comp1 = line[:rucksack_size/2]
    comp2 = line[rucksack_size/2:]

    # Probably not the nicest, but it'll work
    dupe_char_code = 0
    for c in comp1:
        if c in comp2:
            dupe_char_code = ord(c)
            break
    if LOWER_START <= dupe_char_code <= LOWER_END:
        total_priority += dupe_char_code + LOWER_OFFSET
    else:
        total_priority += dupe_char_code + UPPER_OFFSET

print("Done. Total priority of duped items is: " + str(total_priority))