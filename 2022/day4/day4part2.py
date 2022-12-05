f = open(r"C:\Code\advent\2022\day4\day4Input.txt")

overlapping_sections = 0

for line in f:
    elf1, elf2 = line.split(',')
    elf1_range = elf1.split('-')
    elf2_range = elf2.split('-')
    elf1_start = int(elf1_range[0])
    elf1_end = int(elf1_range[1])
    elf2_start = int(elf2_range[0])
    elf2_end = int(elf2_range[1])

    # If I properly thought about it, there's probably a cheaper way to do this, but whatever
    if elf2_start <= elf1_start <= elf2_end or \
        elf2_start <= elf1_end <= elf2_end or \
        elf1_end <= elf2_start <= elf1_end or \
        elf1_start <= elf2_end <= elf1_end:
        overlapping_sections += 1

print("Overlapping sets: " + str(overlapping_sections))